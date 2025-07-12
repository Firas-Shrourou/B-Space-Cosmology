%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% B-Space Cosmology Master Class File
% Filename: BSpacePaper.cls
% Author: Firas Shrourou (with AI assistance)
% Date: July 2025
% Purpose: Provides a single, unified style for all B-Space papers.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{BSpacePaper}[2025/07/11 B-Space Standard Paper Class]

% --- LOAD BASE CLASS AND PACKAGES ---
\LoadClass[11pt, a4paper]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{amsmath, amssymb}
\RequirePackage{geometry}
\RequirePackage{booktabs}
\RequirePackage{siunitx}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage[authoryear,longnamesfirst]{natbib}
\RequirePackage{hyperref}
\RequirePackage{setspace}
\RequirePackage{caption}
\usepackage{xcolor}

% --- PAGE GEOMETRY ---
\geometry{a4paper, margin=1in, headheight=15pt}
\onehalfspacing

% --- HEADER/FOOTER SETUP ---
% This will be applied to ALL documents using this class.
\pagestyle{fancy}
\fancyhf{} % Clear all header and footer fields first
\renewcommand{\headrulewidth}{0pt} % Ensure there is no line in the header
\lfoot{\small © 2025 Firas Shrourou. This work is licensed under a \href{http://creativecommons.org/licenses/by/4.0/}{CC BY 4.0}.}
\rfoot{\thepage} % Place the page number in the right footer

% --- CUSTOM COMMANDS ---
\newcommand{\lcdm}{\(\Lambda\)CDM}
\newcommand{\bspace}{B-Space}
\newcommand{\drip}{Drip}

% --- METADATA HANDLING ---
% Define commands to hold the unique metadata for each paper
\newcommand{\papertitle}[1]{\def\@papertitle{#1}}
\newcommand{\paperauthor}[1]{\def\@paperauthor{#1}}
\newcommand{\papersubject}[1]{\def\@papersubject{#1}}
\newcommand{\paperkeywords}[1]{\def\@paperkeywords{#1}}

% Apply the metadata using hyperref
\AtBeginDocument{
  \hypersetup{
      pdftitle={\@papertitle},
      pdfauthor={\@paperauthor},
      pdfsubject={\@papersubject},
      pdfkeywords={\@paperkeywords},
      pdflang={en},
      colorlinks=true,      % This is the key: color the text, not the border
      linkcolor=blue,       % Color for internal links (e.g., ToC)
      citecolor=blue,       % Color for bibliography citations
      urlcolor=blue,        % Color for external URLs
      pdfborder={0 0 0},    % Explicitly set border width to 0
  }
}

% --- UNIFIED TITLE BLOCK ---
\newcommand{\makeBSCSsupplementtitle}{
    \title{\textbf{\@papertitle}}
    \author{\@paperauthor}
    \date{July 2025}
    \maketitle
    \thispagestyle{fancy}
}

\endinput