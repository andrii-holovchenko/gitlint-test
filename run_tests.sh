#!/bin/bash
#===============================================================================
#
#          FILE:  run_tests.sh
# 
#         USAGE:  ./run_tests.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Andrii Holovchenko (), andriih@mellanox.com
#       COMPANY:  Mellanox Technologies
#       VERSION:  1.0
#       CREATED:  04/16/2020 07:52:25 AM UTC
#      REVISION:  ---
#===============================================================================

RED="\033[31m"
YELLOW="\033[33m"
BLUE="\033[94m"
GREEN="\033[32m"
NO_COLOR="\033[0m"

run_git_check(){
    echo -ne "Running gitlint...${RED}"
    RESULT=$(gitlint 2>&1)
    local exit_code=$?
    handle_test_result $exit_code "$RESULT"
    # FUTURE: check if we use str() function: egrep -nriI "( |\(|\[)+str\(" gitlint | egrep -v "\w*#(.*)"
    return $exit_code
}

handle_test_result(){
    EXIT_CODE=$1
    RESULT="$2"
    # Change color to red or green depending on SUCCESS
    if [ $EXIT_CODE -eq 0 ]; then
        echo -e "${GREEN}SUCCESS"
    else
        echo -e "${RED}FAIL"
    fi
    # Print RESULT if not empty
    if [ -n "$RESULT" ] ; then
        echo -e "\n$RESULT"
    fi
    # Reset color
    echo -e "${NO_COLOR}"
}

run_git_check
