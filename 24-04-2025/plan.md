## Task breakdown
- Input: query string `s`
- Existing data: array of all possible strings available (dictionary)
- Output: array containing all strings from the dictionary containing the input query string as the first character(s).

## Solution
- Store input string as variable
- Take dictionary, and ensure it's in a structure that is efficient to search.
  - Split into alphabetised sub-arrays based on the first letter so [[ace,axe],[bed,bee,beach],[change,charge]...] this will reduce the query lookup complexity dramatically as we only need to access the relevant sub-array for the starting letter.
  - Further optimisations could be to group the first and second half of the alphabet for subsequent letters in arrays so you only need to search a tree that is reduced in complexity by up to 50%.
- split the query into sub-strings for each letter to allow us to calculate the position in the dictionary to search for to check for matches.
- Check the dictionary for all matches and return an array of results

## Code
```php
var s = "de";

var dictionary = array(dog, deer, deal);
var sorted_dictionary = sort_dictionary( dictionary );

var result = array();

// an array of each letter to help with incremental searching
var string_to_search = str_split( s );

foreach( string_to_search as letter ) {
    foreach( sorted_dictionary[ str ] as word ) {
        // split word by the pattern "s" and only return a maximum of 1 result
        result = explode( s, word, 1 );

        if( result[0] !== s ) {
            continue;
        }

        return result[] = word;
    }
}

// return the results - a blank array is fine as a return result
return result;

function sort_dictionary( dictionary ) {
    sorted_dictionary = array();

    // 1. alphabetise the array
    sort( dictionary );

    // 2. split array into indexed sub-arrays for each letter
    // for example [d=>[deal, deer, dog]]
    sorted_dictionary = sort_array_by_first_letter( dictionary );
}

function sort_array_by_first_letter( dictionary ) {
    split_dictionary = array();

    foreach dictionary as d {
        split string at first letter as l

        split_dictionary[
            l => [ d ]
        ]
    }

    return split_dictionary;
}
```