# Instructions for use
## Before starting the application
In order to use the application, one needs to download the source code of the application from the most up to date release from [the GitHub repository of the project](https://github.com/MattiKannisto/ot-harjoitustyo). The application uses a MySQL database which needs to be initialized prior to first use of the application. This can be done with command **poetry run invoke initialize**.

### Starting the application
The application can be started from the root folder of the project with command **poetry run invoke start**. This will open a login screen:

![image](/dokumentaatio/login_screen)

One can create a user account by clicking the button 'Create user account' which will open a register screen:

![image](/dokumentaatio/register_screen)

In order to create an account to the application, one needs to give an unique username, password and a directory into which the output files of the application will be save. Once the account has been successfully created, the register screen will be closed and the login screen will be re-opened. If the user gives correct username and password (the application will notify the user if he/she gives incorrect username and/or password), the login screen will be closed and the main screen of the application will be opened:

![image](/dokumentaatio/main_screen)

The buttons for adding and processing DNA fragments will be activated only when the text box for adding a new DNA fragment are filled in or an existing DNA fragment is selected, respectively. When adding a new DNA fragment, the user is required to give a unique name for the fragment. The sequence of the fragment needs also contain only the letters representing naturally occurring nucleotides. If either of these conditions is not met, and also when a fragment can be successfully added, the user is notified of this in the black notification area. Notifications indicating something went wrong are shown in red, successful addition of a DNA fragment in green, successful generation of sequencing primers in blue and successful translation of the DNA fragment into protein sequence in yellow. The DNA fragments (and user account, user account settings, and primers generated) added will be stored in the MySQL database and the user will be able to browse the DNA fragments he/she has already added to the system from the dropdown menu next to the text 'Now processing DNA fragment". The generated protein sequence and sequencing primer files will be stored in the folder specified by the user when creating the user account. This directory can be changed by selecting 'Options' and then 'Settings' which will open a new window showing settings. In this screen the user can also change settings for generating the sequencing primers and also to delete the user account. The user can log out from the application by clicking 'Options' and then 'Logout'. The application can be closed by clicking 'Options' and then 'Exit'.
