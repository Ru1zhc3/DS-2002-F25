#!/bin/bash
set -e
echo 'Refreshing card sets in card_set_lookup/'

for file in card_set_lookup/*.json;do
    SET_ID=$(basename "$file" .json)
    echo 'Updating set: $SET_ID...'
    curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" -o "$file"
    echo "Data written to $file"
done

echo "All card sets have been refreshed."