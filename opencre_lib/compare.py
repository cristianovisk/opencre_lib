import httpx, json
from rich.console import Console

console = Console()


class Map:
    def __init__(self, primary: str, secundary: str):
        self.primary = primary
        self.secundary = secundary
        self.bases = [
            "ASVS",
            "CAPEC",
            "CWE",
            "Cloud Controls Matrix",
            "ISO 27001",
            "NIST 800-53 v5",
            "NIST 800-63",
            "NIST SSDF",
            "OWASP Cheat Sheets",
            "OWASP Proactive Controls",
            "OWASP Top 10 2021",
            "OWASP Web Security Testing Guide (WSTG)",
            "SAMM"
        ]
        if not self._valid_arguments():
            console.print(f"[red bold][-] [white]Arguments invalid: [blink red]{self.primary, self.secundary}")
            console.print(f"[yellow bold][*] [white]Arguments accepted: [yellow]{self.bases}")
            exit(1)
    
    def _valid_arguments(self):
        flagPrimary = False
        flagSecundary = False
        for base in self.bases:
            if base == self.primary:
                flagPrimary = True
        for base in self.bases:
            if base == self.secundary:
                flagSecundary = True
        
        if flagPrimary == True and flagSecundary == True:
            return True
        else:
            return False
    
    def return_compare(self):
        return self.compare
    
    def return_bases(self):
        return self.bases

    def _request_compare(self):
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        params = {
            'standard': [
                f'{self.primary}',
                f'{self.secundary}',
            ],
        }

        response = httpx.get('https://www.opencre.org/rest/v1/map_analysis', params=params, headers=headers)
        # with open('output.json', 'w') as file:
        #     file.write(json.dumps(response.json(), indent=4))
        return response.json()
    
    def generate_table(self):
        self.compare = self._request_compare()
        self.table = []
        for item in self.compare.get('result').keys():
            for path in self.compare.get('result').get(item).get('paths').keys():
                model = {
                    "base": item,
                    "base_type": item.split(":")[0] if len(item.split(":")) > 0 else "",
                    "base_id": item.split(":")[1] if len(item.split(":")) > 1 else "",
                    "base_description": item.split(":")[2] if len(item.split(":")) > 2 else "",
                    "score_relationship": self.compare.get('result').get(item).get('paths').get(path).get('score'),
                    "standard_match": self.compare.get('result').get(item).get('paths').get(path).get('end').get('id'),
                    "standard_name": self.compare.get('result').get(item).get('paths').get(path).get('end').get('name'),
                    "standard_section": self.compare.get('result').get(item).get('paths').get(path).get('end').get('section'),
                    "standard_sectionID": self.compare.get('result').get(item).get('paths').get(path).get('end').get('sectionID'),
                    "standard_subsection": self.compare.get('result').get(item).get('paths').get(path).get('end').get('subsection'),
                }
                self.table.append(model)
        # with open('processed.json', 'w') as file:
        #     file.write(json.dumps(self.table, indent=4))
        return self.table
    
if __name__ == "__main__":
    r = Map(primary="CWE", secundary="ISO 27001").generate_table()
    print(r)
