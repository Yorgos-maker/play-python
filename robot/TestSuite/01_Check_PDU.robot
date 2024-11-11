*** Settings ***
Documentation   "Get PDU status"
Library   ${EXECDIR}/robot/Master.py     ${EXECDIR}
Resource  robot/TestCase/PDU.robot

*** Test Cases ***
01_get_PDU_status
    [Setup]  log  ${EXECDIR}  #C:\Workspace\robot_practice\pythonProject
    TC_Get_Pdu_Status