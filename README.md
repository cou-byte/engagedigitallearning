# Engage Digital Learning

Static site for *Designing Socially Dynamic Digital Learning* by Chaohua Ou (engagedigitallearning.com).
No WordPress, no build step: plain HTML, one stylesheet, one small script.

```
index.html                      Home / book page
blog/index.html                 Blog index (AI & Education)
blog/<slug>/index.html          One folder per post (URLs match the old WordPress paths)
blog/post-template.html         Copy this to start a new post
assets/site.css, site.js        Shared styles and behaviour
images/                         All images (filled by the "Fetch images" workflow, see step 3)
images/manifest.txt             local-name  original-URL, one per line
404.html, CNAME, .nojekyll      GitHub Pages plumbing
_build.py                       Optional: regenerates nav/footer/post cards across pages
```

## Publishing on GitHub Pages (one-time setup)

1. **Create the repository.** On GitHub, New repository → name it `engagedigitallearning` (any name works), Public, no README. Then upload everything in this folder (drag-and-drop on the "uploading an existing file" page, or `git push` if you use git). Make sure the hidden files `.nojekyll` and the `.github` folder are included.

2. **Turn on Pages.** Repository → Settings → Pages → Source: *Deploy from a branch* → Branch: `main`, folder `/ (root)` → Save. In a minute the site is live at `https://<your-username>.github.io/<repo>/`. (Images will be missing until step 3.)

3. **Fetch the images from the old site** *(do this while WordPress is still running)*. Repository → Actions → "Fetch images from old site" → Run workflow. It downloads every file in `images/manifest.txt` into `images/` and commits them. Check the run log for any `MISSING` lines. After this, nothing on the site depends on WordPress.

4. **Point the domain at GitHub.** In Settings → Pages → Custom domain, enter `engagedigitallearning.com` and save (the `CNAME` file already matches). At your domain registrar, set the DNS records GitHub asks for: four `A` records for the apex domain (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) and a `CNAME` record for `www` pointing to `<your-username>.github.io`. Current values are in GitHub's docs: https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site. Once DNS has propagated (minutes to a day), tick *Enforce HTTPS*.

5. **Connect the contact form.** GitHub Pages can't process forms. Sign up at https://formspree.io (free tier is plenty), create a form, and in `index.html` replace `action="#"` on the `<form>` with the endpoint Formspree gives you. Nothing else changes.

6. **Cancel the WordPress hosting** only after the domain resolves to the new site and the images workflow has run. Keep the domain registration itself.

## Writing a new post

1. Copy `blog/post-template.html` to `blog/<new-slug>/index.html`.
2. Edit the title, date, subtitle and body. The page uses these building blocks (all shown in the template): `<h2>` sections, `.callouts` cards for key findings, `<figure class="fig">` for images with captions, `<blockquote class="pull">` for pull quotes, `<ol class="steps">` for numbered frameworks, `<ol class="refs">` for references, and the `.cite` box.
3. Put images in `images/` and reference them as `../../images/<file>`.
4. Add the post to the list on `blog/index.html` and, if you want it on the home page, to the "AI & Education" cards in `index.html` (copy an existing `<article class="post">` block; the home page shows the two most recent).

If you prefer, add the post to the `POSTS` list in `_build.py` and run `python3 _build.py`; it writes the post page and updates the blog index and the home-page cards for you.

## Editing the look

Colours, fonts and spacing are variables at the top of `assets/site.css` (`--paper` is the pale blue band, `--paper-2` white, `--accent` orange, `--hero-bg` the dark header). Dark mode has its own block of values just below.
