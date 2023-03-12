#!/bin/bash

PANEL_NAME="IR Remote"
TOKEN=$(cat ~/.TRIGGERcmdData/token.tkn)
PANEL_ID=$(curl -s \
  --data-urlencode "name=${PANEL_NAME}" \
  "https://triggercmd.com/api/panel/list?token=${TOKEN}" | jq -r .records[0].id)

curl -s \
  --data-urlencode "panel_id=${PANEL_ID}" \
  "https://triggercmd.com/api/panelbutton/list?token=${TOKEN}" > ~/ir_panel.json

COMPUTER_ID=$(cat ~/.TRIGGERcmdData/computerid.cfg)
curl -s \
  --data-urlencode "computer_id=${COMPUTER_ID}" \
  "https://triggercmd.com/api/computer/list?token=${TOKEN}" | jq -r .records[0].name > ~/computer_name.cache

