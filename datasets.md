# Tor Website Fingerprinting Datasets

## Synopsis

> We sincerely thank the authors of **"A Measurement of Genuine Tor Traces for Realistic Website Fingerprinting"** for compiling and publicly sharing this comprehensive index of Tor website fingerprinting datasets.
> To maintain consistency with the organization of the WF Attack and WF Defense sections in this repository, we reorganize and refer to each dataset using the corresponding **attack model** or **defense model** introduced in the associated publication, rather than strictly following the original dataset names. This naming convention provides a unified view across datasets, attacks, and defenses, making it easier to navigate and compare related research.

## Datasets listing

> In this dataset listing, we use the publication year of the corresponding paper as the dataset year.
> \(N_C\) and \(N_I\) denote the number of classes (domains) and the number of instances collected per monitored class, respectively.

| Name | Year | Activity | Activity detailed | User model | Trace generation software | Closed-world \(N_C \times N_I\) | Open-world \(N_C \times N_I\) |  | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1–D7 | 2024 | Web | Tranco top sites | Index page | TBB 10.5; Chrome 112.0 | \(7.4 \times 10^5\) | 100 | 700 | \(4 \times 10^3\) | [Online](https://zenodo.org/records/16607834) |
| CW/OW | Ca. 2024 | Web | Alexa top sites, random subpage | Random subpage (multi-tab) | TBB | \(8.1 \times 10^4\) | 1000 | 10 | \(9.3 \times 10^3\) | [Online](https://zenodo.org/records/13252953) |
| ALEXA-WSC-FG/BG | Ca. 2024 | Web | Alexa top sites, random subpage | Random subpage | TBB 7.5.6 | \(8.6 \times 10^5\) | 9000 | 90 | \(4.5 \times 10^4\) | No |
| GTT23 | 2023 | Any | Real Tor usage | Visited service | Real client software | \(1.4 \times 10^7\) | \(\langle 1.1 \times 10^6 \text{ domains} \rangle\) | | | [On request](https://doi.org/10.5281/zenodo.10620519) |





