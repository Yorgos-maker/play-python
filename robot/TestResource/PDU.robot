*** Settings ***
Documentation  "Test steps deploymet of PDU"

Library  robot/TestLibrary/PDU.py



*** Keywords ***
ITC_Get_Pdu_Status
    get_pdu_status
    log   "PDU has been truned on"