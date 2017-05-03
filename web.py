#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__='Pablo Robles'
__license__='PSFL'

import http.client
import http.server
import json


class OpenFDAClient():

    OPENFDA_API_URL='api.fda.gov'
    OPEN_API_EVENT='/drug/event.json'
    OPEN_API_SEARCH = "?limit=10&search=patient.drug.medicinalproduct:"
    OPEN_API_SEARCH_COMPANY="?limit=10&search=companynumb:"
    LIMIT="?limit="

    def get_event(self, limit=10):
        conn= http.client.HTTPSConnection(self.OPENFDA_API_URL)
        conn.request('GET', self.OPEN_API_EVENT+ self.LIMIT+str(limit))
        r1= conn.getresponse()
        data1=r1.read()
        events=data1.decode('utf-8')
        return events

    def get_event_search_drug(self,drug):
        conn= http.client.HTTPSConnection(self.OPENFDA_API_URL)
        conn.request('GET', self.OPEN_API_EVENT+self.OPEN_API_SEARCH + drug)
        r1= conn.getresponse()
        data1=r1.read()
        events1=data1.decode('utf-8')
        return events1

    def get_event_search_company(self,company):
        conn= http.client.HTTPSConnection(self.OPENFDA_API_URL)
        conn.request('GET', self.OPEN_API_EVENT+self.OPEN_API_SEARCH_COMPANY + company)
        r2= conn.getresponse()
        data2=r2.read()
        events2=data2.decode('utf-8')
        return events2


class OpenFDAParser():

    def get_drugs_from_event(self, events):

        event_html=''
        drugs=[]
        for i in events:
            drug=(i['patient']['drug'][0]['medicinalproduct'])
            drugs+=[drug]
        return drugs


    def get_companies(self,events):
        companies_list=[]
        for event in events:
            companies_list+=[event['companynumb']]
        return companies_list


    def get_gender_patients(self, events):
        genders_list=[]
        for event in events:
            gender=(event['patient']['patientsex'])
            genders_list+=[gender]
        return genders_list


    def get_better_gender_patients(self, lists):
        gender_list_words=[]
        contador=0
        for i in lists:
            contador+=1
            if contador<(len(lists)+1):
                if i == '1':
                    i='MAN'
                    gender_list_words+=[i]
                elif i == '2':
                    i='WOMAN'
                    gender_list_words+=[i]

        return gender_list_words

    def get_limit(self,path):
        limit=str(path.split('=')[1])
        if limit=='':
            limit=10
        return limit


    def string_to_diccionary(self,limit):
        events=OpenFDAClient().get_event(limit)
        events=json.loads(events)
        if 'results' not in events:
            return 'html'
        else:
            events=events['results']
            return events


    def string_to_diccionary_second(self,funtion):
        events=json.loads(funtion)
        if 'error' in events:
            print (events)
            return 'html'
        else:
            events=events['results']
            return events

    def out_index(self):
        if results not in events:
            html="""
            Has escrito algo mal, vuelve a la página principal
            """
        return html



class OpenFDAHTML():

    def get_main_page(self):
        html= """
        <html>
            <head>
                <div style= "color:#696E6A;text-align:center">
                    <tittle style="font-family: times, serif; font-size:56pt; font-style:oblique">
                    OpenFDA Cool App
                    </tittle>
                </div>

            </head>
            <body>
            <body style="background-color:#918987"> </body style>

                <h1>OpenFDA Client</h1>

                <form method='get' action= 'listDrugs'>
                    <input type='submit' value='Recieve drugs list'>
                    </input>

                    Limit:
                    <input type='text' name='Limit'>
                    </input>

                </form>

                <form method='get' action= 'searchDrug'>
                    <input type='text' name='drug'>
                    </input>
                    <input type='submit' value='Drug Search'>
                    </input>
                </form>

                <form method='get' action= 'listCompanies'>
                    <input type='submit' value='Recieve companies list'>
                    </input>

                    Limit:
                    <input type='text' name='Limit'>
                    </input>
                </form>

                <form method='get' action= 'searchCompany'>
                    <input type='text' name='company'>
                    </input>
                    <input type='submit' value='Company Search'>
                    </input>
                </form>


                <form method='get' action= 'listGender'>
                    <input type='submit' value='Recieve the patients gender'>
                    </input>

                    Limit:
                    <input type='text' name='Limit'>
                    </input>
                </form>

            </body>
        </html>
        """
        return html


    def get_second_page(self, drugs):

        page_html="""
        <html>
            <head>
                <div style= "font-family: times, serif; font-size:36pt; color:#DDC284;text-align:center">
                    <tittle> Items list </tittle>
                </div>
            </head>
            <body>
            <body style="background-color:#918987; max-depth: 500px"> </body style>
                <ol style=" color:#DDC284; text-align:center; font-family: times, serif; font-size:24pt; font-style:bold">
        """

        for drug in drugs:
            page_html+= '<li>' + drug + '</li>\n'

        page_html+= """
                </ol>
            </body>
        </html>
        """
        return page_html


    def get_error_404(self):
        html="""
        <html>
            <head>
            <div style= "color:#696E6A">
                <p style="font-family:courier"> <tittle> ERROR 404 </tittle> </p>
            </div>
            </head>
            <head>
                <tittle style  = "color:#DDC284; text-align:center; font-family: times, serif; font-size:24pt; font-style:bold""> </body style>>
                Has escrito un URL no válida, vuelve a la página principal
                </tittle>
            </head>
            <body style = "background-color:#918987; max-depth: 500px">
                <a href='/'> Click para volver a la página principal </a>
            </body>
        </html>
        """
        return html

    def get_out_index(self):
        html="""
        <html>
            <head>
            <div style= "color:#696E6A">
                <p style="font-family:courier"> <tittle> Estas fuera de rango </tittle> </p>
            </div>
            </head>
            <head>
                <tittle style=" color:#DDC284; text-align:center; font-family: times, serif; font-size:24pt; font-style:bold">
                Has escrito algo mal, vuelve a la página principal
                 </tittle>
            </head>
            <body style = "background-color:#918987; max-depth: 500px">
                <a href='/'> Click para volver a la página principal </a>
            </body>
        </html>
        """

        return html




class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        CLIENT=OpenFDAClient()
        LOGIC=OpenFDAParser()
        HTML=OpenFDAHTML()


        main_page=False
        list_Drugs=False
        is_drug_search = False
        list_Companies=False
        is_company_search= False
        list_Genders=False
        redirect= False
        secret=False



        if self.path=='/':
            main_page= True

        elif '/listDrugs' in self.path:
            list_Drugs= True

        elif 'searchDrug' in self.path:
            is_drug_search = True

        elif '/listCompanies' in self.path:
            list_Companies= True

        elif 'searchCompany' in self.path:
            is_company_search = True

        elif '/listGender' in self.path:
            list_Genders=True

        elif '/redirect' in self.path:
            redirect=True

        elif '/secret' in self.path:
            secret=True




        response=200
        header1='Content-type'
        header2='text/html'

        if main_page:
            html_second=HTML.get_main_page()

        elif list_Drugs:
            path=self.path
            limit=LOGIC.get_limit(path)
            events=LOGIC.string_to_diccionary(limit)
            if events!='html':
                drug=LOGIC.get_drugs_from_event(events)
                html_second=HTML.get_second_page(drug)
            else:
                html_second= HTML.get_out_index()



        elif is_drug_search:
            drug=self.path.split('=')[1]
            events=CLIENT.get_event_search_drug(drug)
            events=LOGIC.string_to_diccionary_second(events)
            if events!='html':
                companies_list=LOGIC.get_companies(events)
                html_second= HTML.get_second_page(companies_list)
            else:
                html_second= HTML.get_out_index()



        elif list_Companies:
            path=self.path
            limit=LOGIC.get_limit(path)
            events=LOGIC.string_to_diccionary(limit)
            if events!='html':
                companies_list=LOGIC.get_companies(events)
                html_second=HTML.get_second_page(companies_list)
            else:
                html_second= HTML.get_out_index()



        elif is_company_search:
            company=self.path.split('=')[1]
            events=CLIENT.get_event_search_company(company)
            events=LOGIC.string_to_diccionary_second(events)
            if events!='html':
                drugs_list=LOGIC.get_drugs_from_event(events)
                html_second=HTML.get_second_page(drugs_list)
            else:
                html_second= HTML.get_out_index()



        elif list_Genders:
            path=self.path
            limit=LOGIC.get_limit(path)
            events=LOGIC.string_to_diccionary(limit)
            genders_list=LOGIC.get_gender_patients(events)
            if events!='html':
                genders_better_list=LOGIC.get_better_gender_patients(genders_list)
                html_second=HTML.get_second_page(genders_better_list)
            else:
                html_second= HTML.get_out_index()



        elif redirect:
            response=302
            header1='Location'
            header2='http://localhost:8000/'

        elif secret:
            response=401
            header1='WWW-Authenticate'
            header2='Basic realm = "My realm"'

        else:
            response=404
            html_second=HTML.get_error_404()
            header1='Content-type'
            header2='text/html'


        self.send_response(response)
        self.send_header(header1, header2)
        self.end_headers()

        if response == 200 or response== 404:
            self.wfile.write(bytes(html_second,'utf-8'))
