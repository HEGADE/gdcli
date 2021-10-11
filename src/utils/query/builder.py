def exclude_site(site: str) -> str:
    url = ""
    if site:
        if len(site.split(",")) > 1:
            sitesArray = site.strip().split(",")
            for site_e in sitesArray:
                if site_e:
                    url += f'-"{site_e}" '
    return f'-"{site}"' if not url else url


if __name__ == "__main__":
    exclude_site(None)
