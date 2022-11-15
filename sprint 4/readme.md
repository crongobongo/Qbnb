# Updates

## Day 1

Dallin  1. Working on dallin_branch
        2. 3 register test cases written (input testing)
        3. test_models.py was breaking my front end testing as it 
        locks the database for some reason. It has been placed 
        in folder "test_models_needs_to_be_fixed" as to not interefere 
        with the frontend testing, as I cannot figure out the bug at this point.
        4. Going to finish the rest of the test cases.

Christian
        1. Worked on christian_branch
        2. Just reviewed the types of test cases

## Day 3

Christian
        1. Just made the functionality test cases, no roadblocks

## Day 5

Christian
        1. Finished the output cases, no roadblocks

## Day 9

Benj    1. Working on bengo_branch
        2. All test cases written (input, output, functionality testing)
        2. Realized that although the user can't update the email or date,
        it was still left up as a text box to be possibly typed in on the html
        page, has been removed now.
        4. Had to change functionality in the models.py and test_models.py
        to accept "N/A" as a string since empty string was not accepted as a
        proper update.
        5. Had to edit functionality in models.py, a part of price was nested
        inside description in the update listing function that was bug-breaking.
        The if statement for price < 10 and >10000, was accidentally nested into
        the description part which would sometimes return None for a correct 
        description and broke the testing in test_update_listing.

Christian
        1. Finished the input cases, small roadblocks fixed in the correct functionality testing
        2. Running correctly on Pytest and Flake8
        3. Pushed all my code to the christian_branch

Will
        1. Working on will_branch
        2. Fixed test case that caused internal server error
        3. Fixed email checking in update profile