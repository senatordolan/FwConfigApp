#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import FwCfgGenMain_ui


# class that implements the firewall configuration generator
class FwCfgGen(QMainWindow, FwCfgGenMain_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # connect up close menu action with local close operation
        self.acActionClose.triggered.connect(self.close)

        # connect up clear forms menu action with clear_forms class member
        self.acClearForms.triggered.connect(self._clearForms)

        # connect up generate button with generate class member
        self.pbGenerate.clicked.connect(self._generate)

        # connect up line edit format reset to clear 'error'
        # formatting when new values are entered into a line edit
        self.leLocalId.textChanged.connect(self._clearLocalIdFormatting)
        self.leRssId.textChanged.connect(self._clearRssIdFormatting)

        # connect up like input variables that should
        # match between both the local and remote settings
        # (mtu, pre-shared key, and encryption

        # mtu
        self.leLocalMtuSize.textChanged.connect(self.leRssMtuSize.setText)
        self.leRssMtuSize.textChanged.connect(self.leLocalMtuSize.setText)

        # pre shared key
        self.leLocalPsk.textChanged.connect(self.leRssPsk.setText)
        self.leRssPsk.textChanged.connect(self.leLocalPsk.setText)

        # encryption
        self.cbLocalEncryption.currentIndexChanged.connect(self.cbRssEncryption.setCurrentIndex)
        self.cbRssEncryption.currentIndexChanged.connect(self.cbLocalEncryption.setCurrentIndex)


    def _clearLocalIdFormatting(self):
        palette = QPalette()
        palette.setColor(QPalette.Text, Qt.black)
        self.leLocalId.setPalette(palette)


    def _clearRssIdFormatting(self):
        palette = QPalette()
        palette.setColor(QPalette.Text, Qt.black)
        self.leRssId.setPalette(palette)

    def _clearForms(self):
        # ------------------------------------------------------------------------
        # _clearForms
        #
        #
        # ------------------------------------------------------------------------

        # clear out all the form data

        # harvest local firewall input values
        self.leLocalId.clear()
        self.leLocalLinkNetwork.clear()
        self.cbLocalEncryption.setCurrentIndex(0)
        self.leLocalMtuSize.clear()
        self.leLocalPsk.clear()
        self .cbLocalFwModel.setCurrentIndex(0)

        # harvest remote firewall input values
        self.leRssId.clear()
        self.leRssLinkNetwork.clear()
        self.cbRssEncryption.setCurrentIndex(0)
        self.leRssMtuSize.clear()
        self.leRssPsk.clear()
        self.cbRemoteFwModel.setCurrentIndex(0)



    def _generate(self):
        # ------------------------------------------------------------------------
        # _generate
        #
        #
        # ------------------------------------------------------------------------

        # harvest local firewall input values
        local_id = self.leLocalId.text()
        local_link_net = self.leLocalLinkNetwork.text()
        local_encryption = self.cbLocalEncryption.currentText()
        local_mtu = self.leLocalMtuSize.text()
        local_psk = self.leLocalPsk.text()
        local_model = self .cbLocalFwModel.currentText()

        # harvest remote firewall input values
        remote_id = self.leRssId.text()
        remote_link_net = self.leRssLinkNetwork.text()
        remote_encryption = self.cbRssEncryption.currentText()
        remote_mtu = self.leRssMtuSize.text()
        remote_psk = self.leRssPsk.text()
        remote_model = self.cbRemoteFwModel.currentText()

        # validate IP address received from GUI
        if False == _validate_ip_address(local_id):

            # highlight incorrect field in red
            palette = QPalette()
            palette.setColor(QPalette.Text, Qt.red)
            self.leLocalId.setPalette(palette)

            # Provide message telling user that provided IP is invalid
            print("local ID invalid")

        if False == _validate_ip_address(remote_id):

            # highlight incorrect field in red
            palette = QPalette()
            palette.setColor(QPalette.Text, Qt.red)
            self.leRssId.setPalette(palette)

            # Provide message telling user that provided IP is invalid
            print("remote ID invalid")



        # temporary debug feedback - remove once real file generation stuff lands here.
        print("Generate button pushed")
        local_fw_config = "Local Values\n"
        local_fw_config += ("%s, %s, %s, %s, %s, %s" % (local_id, local_link_net, local_encryption, local_mtu, local_psk, local_model))
        self.tbLocalFirewallConfig.setText(local_fw_config)

        remote_fw_config = "Remote Values\n"
        remote_fw_config += ("%s, %s, %s, %s, %s, %s" % (remote_id, remote_link_net, remote_encryption, remote_mtu, remote_psk, remote_model))
        self.tbRemoteFirewallConfig.setText(remote_fw_config)


def _validate_ip_address(ip_address):
    # ------------------------------------------------------------------------
    # _validate_ip_address
    #
    # This is a helper method that will be used to determine if the provided
    # string represents a valid IP address.  Function is expecting a string
    # to be provided in the form of 'xxx.xxx.xxx.xxx' where each octet is a
    # string representation of an integer value in the range of 0-255
    # (inclusive).
    #
    # args:
    #   ip_address - string representation of an ip address in the form of
    #                'xxx.xxx.xxx.xxx'
    #
    # returns:
    #   True if the string represents a valid IP address, otherwise will
    #   return False
    # ------------------------------------------------------------------------

    # break ip address up and make sure each octet is at least a number
    octets = [int(x) for x in ip_address.split('.') if x.isdigit()]

    # check that we have four octets that were numbers and if
    # we do move on to validating the range of each octet
    if len(octets) != 4:
        # set return value to indicate that IP address is not valid
        return False
    else:
        # check range of each octet and return roll up status
        octect_status = [_validate_ip_octet(x) for x in octets]
        return all(octect_status)


def _validate_ip_octet(ip_octet):
    # ------------------------------------------------------------------------
    # _validate_ip_octet
    #
    #
    # ------------------------------------------------------------------------

    min_ip_oct = 0
    max_ip_oct = 255
    return (ip_octet >= min_ip_oct) and (ip_octet <= max_ip_oct)


def main(args):

    # create an instance of the app and launch it!
    app = QApplication(sys.argv)
    fcg = FwCfgGen()
    fcg.show()
    app.exec_()


if __name__ == '__main__':
    #  pass sys args to main removing script name
    #  this is being done to support automated testing of the main function
    main(sys.argv[1:])