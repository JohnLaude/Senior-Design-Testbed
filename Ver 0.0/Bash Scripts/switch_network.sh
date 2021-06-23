#!/bin/bash
wpa_cli select network $1
wpa_cli save_config

