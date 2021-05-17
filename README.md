# CITS3403 Group Project

## Project: Build a fitness web app that teaches nutrition & physical exercises

## Sections

[Project Overview](#project-overview)

[Git setup](#gitsetup)

[Branching](#branching)

[Running The Web App](#running-the-web-app)

[Folder structure](#folder-structure)

[Other](#other)

### Project Overview
The goal of this project is to develop a web-based platform, where users can learn about nutrition and physical exercises for different types of fitness goals. Users can then take short quizes/assessments on what they learn and also track & save any progress they make over time.

The material on the page needs to be:
* Informative
* Reliable 
* Intuitive
* Engaging

Some of the functionalities we will require are:
* Users should be able to view the material, save progress, complete assessments & see the results of the completed assessments along with some feedback
* Users should also be able to view aggregate assessment results and usage statistics

Additionally the website requires at least six pages/sections - as outlined by project spec sheet:
* One promoting the theme and purpose to users
* A registration/login page for new or returning users
* One or ore pages presenting content to users
* One or more pages for users to complete assessments
* One page giving feedback to users
* One page showing aggregate results & usage statistics

#### Features
* Login Page - Remember credentials for future autologin, Forgot password, need an account?
* User Registration page - Ask if they already have an account
* User not loged in can only have access to the home page. To access other pages they need to be loged in.
* If user is not logged in and tries to access a restricted page, remember that page, redirect the user to the login page, after successfull login, redirect the user to the page they wanted to access.
* ... To be added...

## Development Environment

### git setup
Since we are using git to collaborate it is important that you get familiar with branching, rebasing, merging & pull requests in order to keep the workflow smooth.

Make sure that you have forked this repo. Once you have forked it, clone it to your desktop.
You can do this by using the gitHub desktop app which can be found over at [desktop.github.com](https://desktop.github.com/).
If you prefer to use git in terminal then change into the directory you want the cloned repo in and run the ```git clone``` command followed by the url for your forked repo. For me this would look like:
```https://github.com/Abdi-Isse/Project.git ```

Once you have done that you want to make sure that the remote for your repo is set up right. Run the following command from the directory of where your cloned repo is:
```git remote -v```

You should see an output that looks similar to this:
<pre><code>origin           https://github.com/Abdi-Isse/Project.git  (fetch)
origin           https://github.com/Abdi-Isse/Project.git  (push)
upstream         https://github.com/CITS3403-Project/Project.git  (fetch)
upstream         https://github.com/CITS3403-Project/Project.git  (push)</code></pre>

Your upstream should be  CITS3403-Project/Project.git and your origin should be your forked repo. If this is not the case then you need to run the following command:
```git remote add upstream  https://github.com/CITS3403-Project/Project.git ```
this will set up the correct upstream repo for you.

It is important to always run the following commands before you start working on making any changes in your local environment:

<pre><code>git fetch upstream
git rebase upstream/main
git push origin main
</code></pre>

The first command will fetch the most up to date version of the upstream repo.
The second command will make sure that your main branch is up to date with the upstream repo.
The third command will push your up to date main branch to your cloned repo on github so that they become the same.

This will help avoid any merge conflicts, which are a pain to fix at times. It will also incorporate any changes that have been added to the main upstream repo into your forked one.

### Branching

The first thing you should do before writing any code is to make sure your local environment is up to date, and to also create a new branch on which to make your changes. Avoid writing code directly from your main branch. To make a new branch run the following command followed by the name you want to give your branch:

```git checkout -b your-new-branch-name```

This command will create a new branch and at the same time move to the new branch. To move between branches use the following command followed by the branch you want to change to:

```git checkout the-branch-name-you-want-to-switch-to```

Once you are done making changes to code and you are happy for it to be added to the codebase, you will need to stage all your changes. This command will stage them:

```git add .```

Once you have staged your changes you will need to commit your changes. To do this run the following command followed by a short description of the changes you have made. For example:

```git commit -m "Added new image classification function"```

Now you are ready to push your changes up to your origin. To do this use the following command followed by the name of the branch you are pushing up to your origin. If you are working on a branch called "classification-tool" then the command would be:

```git push origin classification-tool```

Once you have done this, you should go onto github, go inside of either your forked repo or the upstream repo, and you should see a green button asking you to create a pull request. Once youve made your pull request someone will need to review and approve your changes. Once they are approved, click squash and merge to merge your commits into the codebase.

If the reviewer notices that there are any potential bugs or some minor typo or any other bugs, they should leave a comment on the file and line number where that bug is. This way itll be easier for the person who made the changes to fix them up.

The nice thing about pull requests is that if you need to make any changes, you just simply go back into your local environment and make the changes on the branch that you used to create the pull request. This way, once you are done squashing the bugs/typos and you push the same branch back up, the pull request will update with the new changes added. Then just get it reviewed again.

### Running The web app
Make sure you have python 3 installed. If you dont have it you can download it from [python.org](https://www.python.org/downloads/).

In the project folder you will see that there is a ```scripts``` directory. This directory contains three different files at the moment. Currently you can run this web app using docker or run it locally.

To run the app locally first you need to resolve all the required dependencies by running the build script like this:

```shell
./scripts/build.sh
```

This script will install all the missing dependencies that you require from the ```requirements.txt``` file. If you are using a dependency that is not listed in this file then add the new dependency to the file.

Once you have all the required dependencies you can go ahead and run the app like this:

```shell
./scripts/run.sh
```

If you get an error after running these scripts that looks like this:

```shell
zsh: permission denied: ./scripts/filename.sh
```

Then it means you dont have execution permissions and you will need to give the script execution permission by running:

```shell
chmod u+x ./scripts/filename.sh
```

Alternatively you can run the app fully from docker by running the ```build-and-run-docker.sh``` script like this:

```shell
./scripts/build-and-run-docker.sh
```

To run the app from docker you will need to install docker on your machine which you can do from [here](https://www.docker.com/products/docker-desktop).

If you are not familiar with docker then read up on the [Docker Documentation](https://docs.docker.com/get-started/overview/). (Althought this is not really necessary but it is useful to know how to use docker as it makes working in teams a lot easier).

If you are running the web app with: ```app.run()```, then anytime you make changes to your code you would have to kill and re-run the program. To avoid this run the web app in debug mode, that way in order to see the changes you make you just need to refresh the page. You can do this by using: ```app.run(debug=True)```

Just dont forget to change it back to ```app.run()``` before you put up a pull request.

### Folder structure

Our folder structure will closely follow the specifications outlined in the flask [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/). There is also more information available in Flasks [Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/) docs.

All ```HTML``` files will live inside of the ```Templates folder```, all images, css files & JavaScript files will live inside of the ```static``` folder.

### Resources
[Docker Documentation](https://docs.docker.com/get-started/overview/)

[Flask Documentation](https://flask.palletsprojects.com/)

### Database Structure
![Image of Database Entity-Relation Diagram](https://i.imgur.com/HP6TeDm.png)<br />
Pictured is the database schema for our web-app in ```models.py``` <br />
<br />
```User``` table - Stores the data for user information.<br />
```Score``` table - Stores user score information <br />


### Other

Feel free to update this doc if you think its missing stuff!


