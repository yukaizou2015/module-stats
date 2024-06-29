# Lesson template for ReproNim teaching sessions

How to use this template:

1. Go to the <a href="http://import.github.com/new?import_url=https://github.com/ReproNim/lesson-template
" target="_blank"> Github Importer</a>. In the top text box paste the url of this repo. In the bottom part
choose either "ReproNim" (if that's an option) or your own user account and
then enter the name of the lesson/repository that you wish to create.

2. Change the following variables in the `_confi
.yml` file:
   - `title`
   - `repo`
   - `root`
   - `email` (you can leave Ariel's address here, if you want).
   - `start_time` : this is the start time in minutes since midnight. For
     example, 9 AM is 540 (60 * 9).

3. Edit the content in the `_episodes` folder, adding images (into
  `assets/img`), code (into `code`), data (into `data`) as needed. Pay
  particular attention to the following:

  - Sections should be named `01-first-part.md`, `02-second-part.md`, etc to be ordered in the schedule.
  - Edit the headers of each of your sections. Editing the duration of both `teaching` and `exercises`
  - Add coffee breaks into the lesson. This keeps the timing of each section
    accurate.

# Running with Docker locally for development

Instead of installing ruby and jekyll, you can use docker to run a live version of your repo locally.
As you make changes, it will recompile the changes and all you will need to do is refresh the browser.

The following command it assumes that you are inside your cloned github repo. Adapted from [this blog](https://dev.to/michael/compile-a-jekyll-project-without-installing-jekyll-or-ruby-by-using-docker-4184):

```
docker run --rm -it --volume="$PWD:/srv/jekyll" --volume="$PWD/vendor/bundle:/usr/local/bundle" \
 --env JEKYLL_ENV=development --platform linux/amd64 -p 4000:4000 jekyll/jekyll:4.0.1 \
 jekyll serve --config _config.yml,_config_dev.yml
```

You should then be able to open the live page at http://localhost:4000/

# Acknowledgment

Please see [LICENSE.md](LICENSE.md) for copyright, license, and how to acknowledge information.
