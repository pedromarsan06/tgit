#!/bin/bash
apt update && apt upgrade -y
pkg update && pkg upgrade -y
pkg install git python unzip zip curl wget cmake make
