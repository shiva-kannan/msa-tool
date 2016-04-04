#!/usr/bin/env bash

script_dir=`dirname $0`
platform=`uname`

function build_ui {
    for file in `find ${script_dir}/.. -iname *.ui`
    do
        echo "Converting ${file}"
        ui_file=`echo ${file} | sed "s|/resources/|/ui/|g" | sed "s|.ui$|.py|"`
        pyside-uic ${file} -o ${ui_file}
    done
}

function build_rcc {
    for file in `find ${script_dir}/.. -iname *.qrc`
    do
        echo "Converting ${file}"
        ui_file=`echo ${file} | sed "s|/resources/|/ui/|g" | sed "s|.qrc$|_rc.py|"`
        pyside-rcc ${file} -o ${ui_file}
    done
}

function build_all {
    echo "Calling build_ui.."
    build_ui
    build_rcc
}

build_all