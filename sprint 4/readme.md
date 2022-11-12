# Updates

## Day 1

Dallin  1. Working on dallin_branch
        2. 3 register test cases written (input testing)
        3. test_models.py was breaking my front end testing as it 
        locks the database for some reason. It has been placed 
        in folder "test_models_needs_to_be_fixed" as to not interefere 
        with the frontend testing, as I cannot figure out the bug at this point.
        4. Going to finish the rest of the test cases.

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