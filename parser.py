from tkinter import (Tk, BOTH, RIGHT, RAISED,
                     BooleanVar, Checkbutton, filedialog)
from tkinter.ttk import Frame, Button, Style
#import threading



class STDFParser(Frame):



    def __init__(self):

        super().__init__()

        self.init_ui()


    def init_ui(self):

        self.master.title("STDF Parser")
        self.pack(fill=BOTH, expand=1)
        self.center_window()


    def center_window(self):

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        width, height = screen_width*0.5, screen_height*0.5

        center_x = (screen_width - width)/2
        center_y = (screen_height - height)/2

        self.master.geometry('%dx%d+%d+%d'
                            %(width, height, center_x, center_y))
        self.show_record_types(width, height)


    def show_record_types(self, width, height):

        self.dtr = BooleanVar()
        self.hbr = BooleanVar()
        self.mir = BooleanVar()
        self.mpr = BooleanVar()
        self.mrr = BooleanVar()
        self.pcr = BooleanVar()
        self.pir = BooleanVar()
        self.prr = BooleanVar()
        self.ptr = BooleanVar()
        self.rdr = BooleanVar()
        self.sbr = BooleanVar()
        self.sdr = BooleanVar()
        self.tsr = BooleanVar()
        self.wcr = BooleanVar()
        self.wir = BooleanVar()
        self.wrr = BooleanVar()

        DTR = Checkbutton(self, text="DTR", variable=self.dtr,
                                command=self.check_box_clicked)
        HBR = Checkbutton(self, text="HBR", variable=self.hbr,
                                command=self.check_box_clicked)
        MIR = Checkbutton(self, text="MIR", variable=self.mir,
                                command=self.check_box_clicked)
        MPR = Checkbutton(self, text="MPR", variable=self.mpr,
                                command=self.check_box_clicked)
        MRR = Checkbutton(self, text="MRR", variable=self.mrr,
                                command=self.check_box_clicked)
        PCR = Checkbutton(self, text="PCR", variable=self.pcr,
                                command=self.check_box_clicked)
        PIR = Checkbutton(self, text="PIR", variable=self.pir,
                                command=self.check_box_clicked)
        PRR = Checkbutton(self, text="PRR", variable=self.prr,
                                command=self.check_box_clicked)
        PTR = Checkbutton(self, text="PTR", variable=self.ptr,
                                command=self.check_box_clicked)
        RDR = Checkbutton(self, text="RDR", variable=self.rdr,
                                command=self.check_box_clicked)
        SBR = Checkbutton(self, text="SBR", variable=self.sbr,
                                command=self.check_box_clicked)
        SDR = Checkbutton(self, text="SDR", variable=self.sdr,
                                command=self.check_box_clicked)
        TSR = Checkbutton(self, text="TSR", variable=self.tsr,
                                command=self.check_box_clicked)
        WCR = Checkbutton(self, text="WCR", variable=self.wcr,
                                command=self.check_box_clicked)
        WIR = Checkbutton(self, text="WIR", variable=self.wir,
                                command=self.check_box_clicked)
        WRR = Checkbutton(self, text="WRR", variable=self.wrr,
                                command=self.check_box_clicked)

        DTR.place(x=width*0.20, y=height*0.70)
        HBR.place(x=width*0.20, y=height*0.75)
        MIR.place(x=width*0.30, y=height*0.70)
        MPR.place(x=width*0.30, y=height*0.75)
        MRR.place(x=width*0.20, y=height*0.60)
        PCR.place(x=width*0.20, y=height*0.65)
        PIR.place(x=width*0.30, y=height*0.60)
        PRR.place(x=width*0.30, y=height*0.65)
        PTR.place(x=width*0.20, y=height*0.50)
        RDR.place(x=width*0.20, y=height*0.55)
        SBR.place(x=width*0.30, y=height*0.50)
        SDR.place(x=width*0.30, y=height*0.55)
        TSR.place(x=width*0.20, y=height*0.40)
        WCR.place(x=width*0.20, y=height*0.45)
        WIR.place(x=width*0.30, y=height*0.40)
        WRR.place(x=width*0.30, y=height*0.45)
        generate_records_button = Button(self, text="Generate Records",
                                               command=self.run_records)
        generate_records_button.pack(side=RIGHT)


    def check_box_clicked(self):

        self.enabled_records = []
        if self.dtr.get() == True:
            self.enabled_records.append('DTR')
        if self.hbr.get() == True:
            self.enabled_records.append('HBR')
        if self.mir.get() == True:
            self.enabled_records.append('MIR')
        if self.mpr.get() == True:
            self.enabled_records.append('MPR')
        if self.mrr.get() == True:
            self.enabled_records.append('MRR')
        if self.pcr.get() == True:
            self.enabled_records.append('PCR')
        if self.pir.get() == True:
            self.enabled_records.append('PIR')
        if self.prr.get() == True:
            self.enabled_records.append('PRR')
        if self.ptr.get() == True:
            self.enabled_records.append('PTR')
        if self.rdr.get() == True:
            self.enabled_records.append('RDR')
        if self.sbr.get() == True:
            self.enabled_records.append('SBR')
        if self.sdr.get() == True:
            self.enabled_records.append('SDR')
        if self.tsr.get() == True:
            self.enabled_records.append('TSR')
        if self.wcr.get() == True:
            self.enabled_records.append('WCR')
        if self.wir.get() == True:
            self.enabled_records.append('WIR')
        if self.wrr.get() == True:
            self.enabled_records.append('WRR')


    def run_records(self):

        print(self.enabled_records)
        #for each_enabled_record in self.enabled_records:
        self.export_records_to_csv(self.enabled_records)
        #print('Done')


    def generate_wafer_map(self):
        from stdf.stdf_reader import Reader
        
        stdf = Reader()

        #'20180605113356_XC806Y050C1C_025_S11E_N_T19-V93K_SC8PZR02S3X106P8.std'
        stdf.load_stdf_file(stdf_file=STDF_FILE)



    def export_records_to_csv(self, enabled_records):

        from stdf.stdf_reader import Reader

        stdf = Reader()

        import sys
        STDF_FILE = sys.argv[1]
        
        stdf.load_stdf_file(stdf_file=STDF_FILE)

        STDF_FILE = STDF_FILE.split('.')[0]

        record_header_written = 0
        record_data = open('%s_records.csv'%(STDF_FILE), 'w', encoding='utf-8')

        for (record_name, header, body) in stdf:
            #for each_enabled_record in enabled_records:
            if ( record_name in enabled_records ) and ( record_name == 'SBR' ):
                """
                if not record_header_written:
                    record_data.write('HEAD_NUM,SITE_NUM,SBIN_NUM,SBIN_CNT,SBIN_PF,SBIN_NAME\n')
                    record_header_written = 1
                """
                head_num = body['HEAD_NUM']
                site_num = body['SITE_NUM']
                sbin_num = body['SBIN_NUM']
                sbin_cnt = body['SBIN_CNT']
                sbin_pf = body['SBIN_PF']
                sbin_pf = sbin_pf.decode('utf-8')
                sbin_name = body['SBIN_NAM']
                sbin_name = sbin_name.decode('utf-8')

                record_data.write('%s,%s,%s,%s,%s,%s,%s\n' %(record_name, head_num, site_num, sbin_num, sbin_cnt, sbin_pf, sbin_name))

            elif ( record_name in enabled_records ) and ( record_name == 'HBR' ):
                """
                if not record_header_written:
                    record_data.write('HEAD_NUM,SITE_NUM,HBIN_NUM,HBIN_CNT,HBIN_PF,HBIN_NAME\n')
                    record_header_written = 1
                """
                head_num = body['HEAD_NUM']
                site_num = body['SITE_NUM']
                hbin_num = body['HBIN_NUM']
                hbin_cnt = body['HBIN_CNT']
                hbin_pf = body['HBIN_PF']
                hbin_name = body['HBIN_NAM']

                record_data.write('%s,%s,%s,%s,%s,%s,%s\n' %(record_name,
                                  head_num, site_num, hbin_num,
                                  hbin_cnt, hbin_pf.decode('utf-8'),
                                  hbin_name.decode('utf-8')))

            elif ( record_name in enabled_records ) and ( record_name == 'DTR' ):
                if not record_header_written:
                    sbr_data = record_data.write('Text Data\n')
                    record_header_written = 1
                data = body['TEXT_DAT']
                record_data.write('%s,%s\n'%(record_name, data.decode('utf-8')))

        record_data.close()
        #print('%s exported to CSV' %each_enabled_record)
        print('Done parsing STDF')


def main():

    root = Tk()
    app = STDFParser()
    root.mainloop()


if __name__ == "__main__":
    main()
