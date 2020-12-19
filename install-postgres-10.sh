#!/usr/bin/env bash

set -ex

echo "Installing Postgres 10"
sudo service postgresql stop
sudo rm /usr/local/var/postgres/postmaster.pid
sudo apt-get remove -q 'postgresql-*'
sudo apt-get update -q
sudo apt-get install -q postgresql-10 postgresql-client-10
sudo cp /etc/postgresql/{9.6,10}/main/pg_hba.conf

echo "Restarting Postgres 10"
sudo service postgresql restart
sudo sleep 5
sudo cat /usr/local/var/postgres/server.log

sudo psql -c 'CREATE ROLE travis SUPERUSER LOGIN CREATEDB;' -U postgres
sudo psql -c 'create database bookstore;' -U postgres