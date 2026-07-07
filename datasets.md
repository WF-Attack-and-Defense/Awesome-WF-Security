# Tor Website Fingerprinting Datasets

## Synopsis

> We sincerely thank the authors of **"A Measurement of Genuine Tor Traces for Realistic Website Fingerprinting"** for compiling and publicly sharing this comprehensive index of Tor website fingerprinting datasets.
> To maintain consistency with the organization of the WF Attack and WF Defense sections in this repository, we reorganize and refer to each dataset using the corresponding **attack model** or **defense model** introduced in the associated publication, rather than strictly following the original dataset names. This naming convention provides a unified view across datasets, attacks, and defenses, making it easier to navigate and compare related research.

## Datasets listing

> In this dataset listing, we use the publication year of the corresponding paper as the dataset year if the dataset collection date was not provided.
> This dataset listing includes only datasets with publicly accessible and valid download links.
> \(N_C\) and \(N_I\) denote the number of classes (domains) and the number of instances collected per monitored class, respectively.

| Name | Year | Activity | Activity detailed | User model | Trace generation software | Closed-world \(N_C x N_I\) | Open-world \(N_C x N_I\) | Multi-tab included? | Download Link |
| --- | --- | --- | --------- | --------- | ------------ | --------------- | --------------- | --------- | --------- | 
| STAR | P2026 | Web | Tranco Top list; Collection location across North America, Europe, and Asia  | Index page | Chrome browser; Selenium; Tor | 150, 000 x 1 | 20, 000 x 1 | No | [Download](https://zenodo.org/records/17060855) |
| HiFi-WF | P2026 | Web | Tranco Top list | Index page; Subpages | Chrome browser; Tor | Homepage-Subpage: 250 x 10 | 12, 000 x 1 | Yes | [Download](https://drive.google.com/file/d/1v86rGzmXOrV2tAGfNvCzhTyi69bZNSUv/view) |
| UDA-WF | P2026 | Web | MAJESTIC Top-Ranking Website | Index page  | TBB v13.0.1; Tor-browser-selenium | 90 x 100 | 9000 x 1 | No | [Download](https://github.com/Lwsy123/UDA-WF) |
| Proteus | 2024-2025 | Web | Tranco Top list; Network Condition Drift dataset collected from Singapore, Japan, the United States, Germany, and the United Kingdom  | Index page; Subpages | Tor-browser-selenium; Tor 0.4.8, 0.4.7, 0.4.6, and 0.4.5; TBB v12.0.10; |  102 monitored websites; Temporal Drift (9 months): 1.4 x 10^5 traces; Tor Version Drift: 1.0 x 10^5 traces; Network Condition Drift: 3.4 x 10^4; Browsing Behavior Drift: 17,739 subpages | 20,000 x 1 | No | [Download](https://drive.google.com/drive/folders/1bAqAvvDrY2wrY4EU-Rxm9mv9hsIvKwGk) |
| Swallow | 2024 | Web | Tranco top sites | Index page | TBB 10.5; Chrome 112.0 | 100 x 100 | 4,000 x 1 | No | [Download](https://zenodo.org/records/16607834) |
| FMWF | P2025 | Web | Top 100 from top.chinaz.com | Index page | Tor browser | 100 x 100; Multi-tab randomly combined |-- | Yes | [Download](https://drive.google.com/drive/folders/1iH-pO2_N-sQmR4AI9yc23R_N0_qvXYyr) |
| CE-450 | P2025 | Web | Alexa top sites | Index page | Selenium | 400 x 50 | 50 x 50 | No | [Download](https://drive.google.com/file/d/1OuHoMh2QmLg5k1ogJROGkTbtgGeVexbT/view?usp=sharing) |
| GTT23 | 2023 | Any | Real Tor usage | Visited service | Real client software | 1.4 x 10^7 (1.1 x 10^6 domains) | Curated manually | No | [Requests](https://doi.org/10.5281/zenodo.10620519) |
| Oscar | P2024 | Web | Alexa top sites, random subpage | Random subpage (multi-tab) | TBB | 81,284 traces | 9,236 traces | Yes | [Download](https://zenodo.org/records/13252953) |
| Drift | P2023 | Web | Popular websites, links from Rimmer et al. | Index page | TBB 11.0.10; tor-browser-selenium 0.6.3 | 90 x ~110 | 5,000 | No | [Download](https://github.com/SPIN-UMass/Realistic-Website-Fingerprinting-By-Augmenting-Network-Traces) |
| ARES | 2022 | Web | Alexa top pages | Index page (multi-tab) | TBB; Selenium | 5.7 x 10^5 traces | -- | Yes | [Download](https://github.com/Xinhao-Deng/Multitab-WF-Datasets) |
| D<sub>tbs, tor</sub> | 2022 | Web | Wikipedia browsing | Random subpage | tor-browser-selenium | 98 x 200 | -- | Yes | [Download](https://explainwf-popets2023.github.io/data/) |
| BigEnough | 2021 | Web | Open PageRank top pages | Index page | TBB | 950 x 20 | 19,000 x 1 | No | [Download](https://drive.google.com/drive/folders/1cRIujmDFUpVD0rA0U92bxeGaq5DMlzFm?usp=drive_link) |
| Good Enough | 2020 | Web | Alexa top pages, random subpage | Index page | TBB 9.0.2 | 500 x 20 | 10,000 x 1 | No | [Download](https://github.com/pylls/padding-machines-for-tor) |
| DF | P2018 | Web | Alexa top sites | Index page | tor-browser-selenium | 95 x 1000 | 40,716 x 1 | No | [Download](https://github.com/deep-fingerprinting/df) |
| AWF <sub>CW<sub>900</sub></sub> | 2017 | Web | Alexa top sites | Index page | tor 0.2.8.11; TBB 6.5; Selenium | 900 x 2500 | -- | No |  [Download](https://github.com/DistriNet/DLWF) |
| AWF Recollect | 2017 | Web | Alexa top sites | Index page | tor 0.2.8.11; TBB 6.5; Selenium | 200 x 500 | -- | No | [Download](https://github.com/DistriNet/DLWF) |
| AWF Open | 2017 | Web | Alexa top sites | Index page | tor 0.2.8.11; TBB 6.5; Selenium | 200 x 2000 | 4 x 10^5 | No | [Download](https://github.com/DistriNet/DLWF) |
| k-NN | P2014 | Web | Sensitive sites, Alexa top sites | Index page | TBB 3.5.1; iMacros 8.6.0 | 90 x 100 | 5 x 10^3 | No | [Download](https://www.cs.sfu.ca/~taowang/wf/data/) |










