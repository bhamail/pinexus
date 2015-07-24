
__author__ = 'bhamail'

import os

import sys
import getopt

import ConfigParser

import subprocess
import getpass


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


section_card = 'card'

def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hc:", ["help", "config"])
        except getopt.error, msg:
            raise Usage(msg)

        # process commandline options
        configfile = "createSDCard.cfg"
        for o, a in opts:
            if o in ("-c", "--config"):
                configfile = a
            if o in ("-h", "--help"):
                print "Usage: python " + __file__ + " -c <configuration file>"

        print "Using configuration file: " + os.path.abspath(configfile)

        # read config file settings
        config = ConfigParser.SafeConfigParser()
        config.read(configfile)

        action = config.get(section_card, 'action')
        image_to_card = (action == "image_to_card")
        card_to_image = (action == "card_to_image")

        if image_to_card or card_to_image:
            password = getpass.getpass("Enter sudo password:")

            if image_to_card:
                burn_osimage_to_card(config, password)

            if card_to_image:
                create_osimage_from_card(config, password)
        else:
            print "Doing nothing. Check config: action."

        return 0

    except Usage, err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"
        return 2


def quote_path(path):
    return '\'' + path.replace(" ", "\ ") + '\''


def unmount_sdcard(config):
    """ unmount sdcard using command configured via: umount_card_cmd """

    umount_card_cmd = config.get(section_card, 'umount_card_cmd')
    output = subprocess.check_output(umount_card_cmd, shell=True)
    print (output)


def burn_osimage_to_card(config, password):
    """ copy os image (config: os_image_path) to sd card (config: card_path) """

    unmount_sdcard(config)

    os_image_path = config.get(section_card, 'os_image_path')
    if not os.path.isfile(os_image_path):
        raise ValueError("Missing os_image_path file : " + os_image_path)

    card_path = config.get(section_card, 'card_path')

    dd_cmd = 'dd bs=1m if=' + quote_path(os_image_path) + ' of=' + quote_path(card_path)

    print('Writing os image to sdcard via: ' + dd_cmd)

    # result = subprocess.check_output(dd_cmd, shell=True)
    result = exec_cmd_with_sudo(dd_cmd, password)

    return result


def create_osimage_from_card(config, password):
    """ create os image from sd card (config: card_path) and store in hdd file (config: os_image_to_create_path) """

    unmount_sdcard(config)

    # copy sdcard contents (all partitions) to .img file
    card_path = config.get(section_card, 'card_path')

    os_image_to_create_path = config.get(section_card, 'os_image_to_create_path')

    dd_cmd = 'dd bs=1m if=' + quote_path(card_path) + ' of=' + quote_path(os_image_to_create_path)

    print('Copying sdcard to os image via: ' + dd_cmd)

    result = exec_cmd_with_sudo(dd_cmd, password)

    return result


def exec_cmd_with_sudo(cmd, password):
    p = subprocess.Popen('sudo -S  -s ' + cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)
    std_out, std_err = p.communicate(password + '\n')
    result = p.wait()
    print(std_out)
    print(std_err)
    print(result)
    if result != 0:
        raise ValueError('cmd broke')
    return result


if __name__ == "__main__":
    sys.exit(main())
