# Python + Selenium - Hyundai


## Install the prerequisite
1. Please go to ```Installation.docx``` to install the prerequisite. (This instruction is intended for Windows only.)


## How to run the test scripts
1. Open a ```Command Prompt```
1. Enter ```workon python364_env```
1. Go to the path where the test scripts located (e.g ```cd Desktop\Hyundai```)
1. Run the test scripts. There are different ways to run the test scripts:
   - ```pytest testscripts\ --html=report.html``` -> this is to run all the test scripts under testscripts folder.
   - ```pytest testscripts\ -k "[name_of_the_test_script]" --html=report.html``` -> this is to run single test script. (e.g. ```pytest testscripts\ -k "test_fifth_slide_image_from_home_page" --html=report.html```)
   - ```pytest testscripts\[test_script_filename] --html=report.html``` -> this is to run all the test scripts under this file (e.g. ```pytest testscripts\test_hyundai_longueuil_images.py --html=report.html```)


Note: ```--html=report.html``` is where you can check the result of the test scripts if it is PASS or FAIL (You can rename the `report.html` whatever name you want.)
