import requests

name = "out"
print(f"::set-output name={name}::my output")


r = requests.get(
    f"https://zenodo.org/api/records/?&sort=mostrecent&page=1&size=1000&all_versions=0&keywords=bioimage.io"
)
print(r.status_code)
print(r.reason)
print(r.json())
