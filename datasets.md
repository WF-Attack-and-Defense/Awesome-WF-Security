# Tor Website Fingerprinting Datasets

## Synopsis

> We sincerely thank the authors of **"A Measurement of Genuine Tor Traces for Realistic Website Fingerprinting"** for compiling and publicly sharing this comprehensive index of Tor website fingerprinting datasets.
> To maintain consistency with the organization of the WF Attack and WF Defense sections in this repository, we reorganize and refer to each dataset using the corresponding **attack model** or **defense model** introduced in the associated publication, rather than strictly following the original dataset names. This naming convention provides a unified view across datasets, attacks, and defenses, making it easier to navigate and compare related research.

## Datasets listing

> In this dataset listing, we use the publication year of the corresponding paper as the dataset year.
> This dataset listing includes only datasets with publicly accessible and valid download links.
> \(N_C\) and \(N_I\) denote the number of classes (domains) and the number of instances collected per monitored class, respectively.

| Name | Year | Activity | Activity detailed | User model | Trace generation software | Closed-world \(N_C x N_I\) | Open-world \(N_C x N_I\) | Multi-tab included? | Download Link |
| --- | --- | --- | --------- | --------- | ------------ | --------------- | --------------- | --------- | --------- | 
| STAR | 2026 | Web | Tranco Top list; Collection location across North America, Europe, and Asia  | Index page | Chrome browser; Selenium; Tor | 150, 000 x 1 | 20, 000 x 1 | No | [Download](https://zenodo.org/records/17060855) |
| HiFi-WF | 2026 | Web | Tranco Top list | Index page; Subpage | Chrome browser; Tor | Homepage-Subpage: 250 x 10 | 12, 000 x 1 | Yes | [Download](https://drive.google.com/file/d/1v86rGzmXOrV2tAGfNvCzhTyi69bZNSUv/view) |
| GTT23 | 2023 | Any | Real Tor usage | Visited service | Real client software | 1.4 x 10^7 (1.1 x 10^6 domains) | Curated manually | No | [Download](https://doi.org/10.5281/zenodo.10620519) |





