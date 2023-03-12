#!/bin/bash
./cache_data.sh
BUTTON=$1
PIPE_TRIGGER=$(cat ~/ir_panel.json | jq '.records[] | select(.name=="'${BUTTON}'")' | jq -r .trigger)
echo $PIPE_TRIGGER
TOKEN=$(cat ~/.TRIGGERcmdData/token.tkn)
COMPUTER_NAME=$(cat ~/computer_name.cache)
SENDER=${SENDER="IR Remote"}

function remote_trigger {
    curl -s \
      --data-urlencode "panel=${SENDER}" \
      --data-urlencode "sender=${SENDER}" \
      --data-urlencode "button=${BUTTON}" \
      "https://triggercmd.com/api/panel/trigger?token=${TOKEN}"
}

# If the trigger is on this computer ...
if [[ $PIPE_TRIGGER = $COMPUTER_NAME* ]]; then
  TRIGGER=$(echo ${PIPE_TRIGGER} | cut -d '|' -f 2 | xargs)
  # If the trigger name starts with ar_ then trigger it remotely to trigger the Alexa Routine.
  if [[ $TRIGGER = ar_* ]]; then
    remote_trigger
  else
    COMMAND=$(cat ~/.TRIGGERcmdData/commands.json | jq ".[] | select(.trigger==\"${TRIGGER}\")" | jq -r .command)
    $COMMAND
  fi
else
  remote_trigger
fi