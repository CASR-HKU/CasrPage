#!/usr/bin/env bash
hugo
tar -cvzf public_html.tar.gz ./public_html
scp public_html.tar.gz casr:~/
