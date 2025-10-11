# resume.md

![Resume](https://raw.githubusercontent.com/mikepqr/resume-markdown/main/example/resume.png)

Write your resume in
[Markdown](https://raw.githubusercontent.com/mikepqr/resume-markdown/main/src/resume_markdown/resume.md),
style it with [CSS](src/resume_markdown/resume.css), output to [`resume.html`](example/resume.html) and
[`resume.pdf`](example/resume.pdf).

## Prerequisites

 - Python ≥ 3.9 or `uv`
 - Optional, required for PDF output: Google Chrome or Chromium

## Installation

### Using uvx (recommended, no installation needed)

Run directly without installing:

```bash
uvx resume-markdown
```

### Using uv tool install (persistent installation)

Install once, use everywhere:

```bash
uv tool install resume-markdown
```

### Using pip

```bash
pip install resume-markdown
```

## Usage

### Quick start

 1. Create template files in your current directory:

    ```bash
    resume-markdown init
    # or with uvx: uvx resume-markdown init
    ```

    This creates [`resume.md`](src/resume_markdown/resume.md) and [`resume.css`](src/resume_markdown/resume.css) in the current directory.

 2. Edit your copy of `resume.md` with your resume content (the placeholder text is taken
    with thanks from the [JSON Resume Project](https://jsonresume.org/themes/))

 3. Build HTML and PDF output:

    ```bash
    resume-markdown build
    # or with uvx: uvx resume-markdown build
    ```

### Build options

 - Use `--no-html` or `--no-pdf` to disable HTML or PDF output:
   ```bash
   resume-markdown build --no-pdf
   ```

 - Use `--chrome-path=/path/to/chrome` if the tool cannot find your Chrome
   or Chromium executable (needed for PDF output)
   ```bash
   resume-markdown build --chrome-path=/path/to/chrome
   ```

 - Specify a custom input file:
   ```bash
   resume-markdown build myresume.md
   ```

## Customization

Edit [`resume.css`](src/resume_markdown/resume.css) to change the appearance of your resume. The
default style is extremely generic, which is perhaps what you want in a resume,
but CSS gives you a lot of flexibility. See, e.g. [The Tech Resume
Inside-Out](https://www.thetechinterview.com/) for good advice about what a
resume should look like (and what it should say).

Change the appearance of the PDF version (without affecting the HTML version) by
adding rules under the `@media print` CSS selector.

Change the margins and paper size of the PDF version by editing the [`@page` CSS
rule](https://developer.mozilla.org/en-US/docs/Web/CSS/%40page/size).
