#! /bin/bash

export MAIL_USERNAME=''
export MAIL_PASSWORD=''

export CONTEST_SUBJECT=''
export CONTEST_RECIP=''
export CONTEST_BODY=''

`dirname $0`/contest.py
