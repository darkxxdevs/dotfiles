#!/usr/bin/env bash
speedtest-cli --simple | awk '/^Download/ {print "   " $2 " Mb/s"} /^Upload/ {print "Up: " $2 " Mb/s"}'

