If you want multiple heroku accounts (ie. One Personal, One for work, One for SmarPower), install Heroku Toolbelt in CLI

https://stackoverflow.com/questions/13140375/heroku-toolbelt-switch-between-multiple-account

Steps:

1. heroku plugins:install heroku-accounts

2. heroku accounts:add "Account-Name"

3. Login to Account




heroku accounts:set "Account-Name" - Switches between your accounts when pushing projects to Heroku
