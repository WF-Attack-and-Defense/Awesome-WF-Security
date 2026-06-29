Index of Tor Website Fingerprinting Datasets


# Index of Tor Website Fingerprinting Datasets

## Synopsis

This data is based off of Table 2 from [Jansen R, Wails R, and Johnson A. A measurement of genuine Tor traces
for realistic website fingerprinting. In: Proceedings of the 27th International
Conference on Passive and Active Measurement (PAM). Springer, 2026.](https://www.rwails.org/research/jansen_pam_26.pdf)

This table indexes major, publicly available datasets used for Tor website
fingerprinting experimentation. If you see an error or have a new dataset to
add, please [submit a
pull request](https://codeberg.org/rwails/tor-wf-index/pulls).

---

## Datasets listing

The \(\bot\) symbol indicates an unnamed dataset. When the year of data collection is not mentioned, we assume it is around ("ca.") the associated article's publication date. \(N\), \(N\_C\), \(N\_I\), \(N\_{Bg}\) are the total number of traces, number of positive classes, instances per positive class, and number of background traces.

| Name | Year | Activity | Activity detailed | User model | Trace generation software | \(\mathit{N}\) | \(\mathit{N\_C}\) | \(\mathit{N\_I}\) | \(\mathit{N\_{Bg}}\) | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \(\bot\) (Hermann) | 2008 | Web | Links from real-world academic proxy server | Index page | Autofox | \(8.5 \times 10^3\) | 775 | \(\approx 10\) |  | [Dead link](https://www-sec.uni-regensburg.de/website-fingerprinting/) |
| \(\bot\) (Cai) | Ca. 2012 | Web | Alexa top sites | Index page | tor 0.2.1/2 | \(3.2 \times 10^4\) | 800 | \(\approx 40\) |  | No |
| levdata2 | Ca. 2013 | Web | Alexa top sites | Index page | tor 0.2.4.7; TBB 2.4.7 | \(4 \times 10^3\) | 100 | 40 |  | [Online](https://www.cs.sfu.ca/~taowang/wf/data/) |
| levdata3 | Ca. 2013 | Web | Popular blocked sites, Alexa top sites | Index page | tor 0.2.4.7; TBB 2.4.7 | \(9 \times 10^2\) | 4 | 10 | \(8.6 \times 10^2\) | [Online](https://www.cs.sfu.ca/~taowang/wf/data/) |
| \(k\)-NN | Ca. 2014 | Web | Sensitive sites, Alexa top sites | Index page | TBB 3.5.1; iMacros 8.6.0 | \(1.4 \times 10^4\) | 100 | 90 | \(5 \times 10^3\) | [Online](https://www.cs.sfu.ca/~taowang/wf/data/) |
| \(\bot\) (Juárez) | Ca. 2014 | Web | Alexa top sites, volunteer browsing | Index page, visited pages | TBB (2/3.X); Selenium | \(4.3 \times 10^4\) | 200 | \(\approx 40\) | \(3.5 \times 10^4\) | On request |
| \(\bot\) (Wang) | 2014 | Web | Sensitive sites, Alexa top sites | Index page | tor 0.3.6.4; TBB 3.6.4 | \(9 \times 10^3\) | 100 | 40 | \(5 \times 10^3\) | No |
| RND-WWW | Ca. 2016 | Web | Twitter, Alexa one-click, Google Trends, Google Random, censored sites | Random subpage | TBB 3.6.1; Chickenfoot; iMacros; Scriptish | \(1.6 \times 10^5\) | 1125 | 40 | \(1.2 \times 10^5\) | [Dead link](http://lorre.uni.lu/~andriy/zwiebelfreunde/) |
| ┅TOR-Exit | Ca. 2016 | Web | HTTP requests of real Tor users | Visited page | TBB 3.6.1; Chickenfoot; iMacros; Scriptish | \(2.1 \times 10^5\) |  |  | \(2.1 \times 10^5\) | [Dead link](http://lorre.uni.lu/~andriy/zwiebelfreunde/) |
| ┅WEBSITES | Ca. 2016 | Web | Popular websites | Index page, random subpage | TBB 3.6.1; Chickenfoot; iMacros; Scriptish | \(5.3 \times 10^3\) | 50 | 105 |  | [Dead link](http://lorre.uni.lu/~andriy/zwiebelfreunde/) |
| \(\mathit{DS\_{Tor}}\) | Ca. 2016 | Web | Alexa top sites, popular .onion sites | Index page | TBB; Selenium | \(1.1 \times 10^5\) | 85 | \(\approx 90\) | \(1 \times 10^5\) | [Dead link](https://github.com/jhayes14/k-FP) |
| AWF \(\mathit{CW\_{900}}\) | 2017 | Web | Alexa top sites | Index page | tor 0.2.8.11; TBB 6.5; Selenium | \(2.3 \times 10^6\) | 900 | 2500 |  | [Online](https://github.com/DistriNet/DLWF) |
| ┅AWF Recollect | 2017 | Web | Alexa top sites | Index page | tor 0.2.8.11; TBB 6.5; Selenium | \(1 \times 10^5\) | 200 | 500 |  | [Online](https://github.com/DistriNet/DLWF) |
| ┅AWF Open | 2017 | Web | Alexa top sites | Index page | tor 0.2.8.11; TBB 6.5; Selenium | \(8 \times 10^5\) | 200 | 2000 | \(4 \times 10^5\) | [Online](https://github.com/DistriNet/DLWF) |
| DF | Ca. 2018 | Web | Alexa top sites | Index page | tor-browser-selenium | \(1.4 \times 10^5\) | 95 | 1000 | \(4.1 \times 10^4\) | [Online](https://github.com/deep-fingerprinting/df) |
| WTT-time | 2018 | Web | Alexa top sites | Index page | tor 0.4.0.8; tor-browser-crawler | \(8 \times 10^4\) | 100 | 300 | \(5 \times 10^4\) | On request |
| \(\bot\) (Wang) | 2019 | Web | Alexa top sites | Index page | tor 0.4.0.1; TBB 8.5a7 | \(1 \times 10^5\) | 100 | 200 | \(8 \times 10^4\) | [Partially Online](https://github.com/literaltao/openwf) |
| ┅Wikipedia | 2019 | Web | Wikipedia browsing | Random subpage | tor 0.4.0.1; TBB 8.5a7 | \(2 \times 10^4\) | 100 | 100 | \(1 \times 10^4\) | [Partially Online](https://github.com/literaltao/openwf) |
| Good Enough | 2020 | Web | Alexa top pages, random subpage | Index page | TBB 9.0.2 | \(2 \times 10^4\) | 500 | 20 | \(1 \times 10^4\) | [Online](https://github.com/pylls/padding-machines-for-tor) |
| GDLF-25 | Ca. 2021 | Web | Alexa top sites | Random subpage | tor-browser-crawler | \(9.4 \times 10^4\) | 2400 | 39 |  | On request |
| ┅GDLF-OW | Ca. 2021 | Web | Links from Rimmer et al. | Random subpage | tor-browser-crawler | \(7 \times 10^4\) |  |  | \(7 \times 10^4\) | On request |
| BigEnough | 2021 | Web | Open PageRank top pages | Index page | TBB | \(3.8 \times 10^4\) | 950 | 20 | \(1.9 \times 10^4\) | On request |
| Multi-tab | 2022 | Web | Alexa top pages | Index page (multi-tab) | TBB; Selenium | \(5.7 \times 10^5\) |  |  |  | [Online](https://github.com/Xinhao-Deng/Multitab-WF-Datasets) |
| \(D(\mathrm{tbs, tor})\) | 2022 | Web | Wikipedia browsing | Random subpage | tor-browser-selenium | \(2 \times 10^4\) | 98 | 200 |  | [Online](https://explainwf-popets2023.github.io/data/) |
| Drift | Ca. 2023 | Web | Popular websites, links from Rimmer et al. | Index page | TBB 11.0.10; tor-browser-selenium 0.6.3 | \(1.5 \times 10^4\) | 90 | \(\approx 110\) | \(5 \times 10^3\) | [Online](https://github.com/SPIN-UMass/Realistic-Website-Fingerprinting-By-Augmenting-Network-Traces) |
| GTT23 | 2023 | Any | Real Tor usage | Visited service | Real client software | \(1.4 \times 10^7\) | \(\langle 1.1 \times 10^6 \text{ domains} \rangle\) | | | [On request](https://doi.org/10.5281/zenodo.10620519) |
| ALEXA-WSC-FG/BG | Ca. 2024 | Web | Alexa top sites, random subpage | Random subpage | TBB 7.5.6 | \(8.6 \times 10^5\) | 9000 | 90 | \(4.5 \times 10^4\) | No |
| CW/OW | Ca. 2024 | Web | Alexa top sites, random subpage | Random subpage (multi-tab) | TBB | \(8.1 \times 10^4\) | 1000 | 10 | \(9.3 \times 10^3\) | [Online](https://zenodo.org/records/13252953) |
| D1–D7 | 2024 | Web | Tranco top sites | Index page | TBB 10.5; Chrome 112.0 | \(7.4 \times 10^5\) | 100 | 700 | \(4 \times 10^3\) | [Online](https://zenodo.org/records/16607834) |
