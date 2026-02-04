SEARCH_PATTERN=$1
OUTPUT=$2
curl https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt -o mobydick.txt
OCCURRENCES=$(grep -o "$SEARCH_PATTERN" mobydick.txt | wc -l)
echo "The search pattern $1 was found $OCCURRENCES time(s)." > "$2"
