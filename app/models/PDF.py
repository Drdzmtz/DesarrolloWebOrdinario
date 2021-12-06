from fpdf import FPDF

class Custom_PDF(FPDF):
        
    def header(self):

        self.set_fill_color(142, 192, 219)
        self.rect(0, 0, 140, 40, "F")

        self.set_fill_color(60, 132, 171)
        self.rect(0, 0, 210, 10, "F")

        self.set_fill_color(16, 71, 107)
        self.rect(0, 0, 10, 100, "F")


        self.image('app/static/images/large-logo.png', 20, 20, 109.25, 10.25)

    def footer(self):
        self.set_fill_color(142, 192, 219)
        self.rect(0, 285, 210, 15, "F")


class PDF():

    def __init__(self, house):
        self.house = house
        self.pdf = Custom_PDF()

    def generate_pdf(self):
        pdf = self.pdf 

        pdf.set_margins(20, 40, 20)
        pdf.add_page()

        x = pdf.get_x()
        y = pdf.get_y()

        pdf.image(self.house.photo, 20, 50, 80, 80)

        pdf.set_font('Arial', 'B', 30)
        pdf.set_xy(150, 10)

        pdf.cell(40, 20, self.house.type, 0, 2, "L", False,  "")
        pdf.cell(40, 10, self.house.status, 0, 1, "L", False,  "")
        
        pdf.set_xy(20,20)
        pdf.set_draw_color(16, 71, 107)
        pdf.set_line_width(5)
        pdf.line(105, 52, 105, 128)
        
        pdf.set_xy(110, 52)
        pdf.set_font('Arial', '', 16)
        pdf.set_text_color(169 ,169, 169)
        pdf.cell(40, 4, "Precio:", 0, 2, "CL", False,  "")
        pdf.set_text_color(0, 0, 0)

        pdf.set_font('Arial', 'B', 30)
        pdf.cell(40, 12, f'{self.house.price} $MXN', 0, 2, "CL", False,  "")

        aux_x = pdf.get_x()
        aux_y = pdf.get_y()

        pdf.set_line_width(1)
        pdf.line(aux_x+2, aux_y, aux_x+95, aux_y)

        pdf.set_font('Arial', '', 12 )
        pdf.set_xy(pdf.get_x()+5, pdf.get_y()+5)
        pdf.multi_cell(90, 7, f'{self.house.description}', 0,  "L", False,  "")
        
        pdf.set_font('Arial', 'B', 16)
        pdf.set_y(pdf.get_y()+40)

        pdf.set_fill_color(228, 234, 236)
        pdf.rect(pdf.get_x(), pdf.get_y(), 210, 10, "F")

        pdf.set_fill_color(240, 241, 242)
        pdf.rect(pdf.get_x(), pdf.get_y()+10, 210, 50, "F")
        pdf.cell(40, 10, f'{self.house.city}, {self.house.state}', 0, 1, "L", False,  "")
        
        pdf.set_font('Arial', '', 14)
        pdf.set_x(pdf.get_x()+5)
        pdf.cell(40, 10, f'Codigo Postal: {self.house.zip_code}', 0, 2, "L", False,  "")
        pdf.multi_cell(100, 10, f'Direccion: {self.house.address}', "", False,  "")
        pdf.cell(40, 10, f'    Longitud: {self.house.longitude}',  0, 2, "L", False,  "")
        pdf.cell(40, 10, f'    Latitud: {self.house.latitude}',  0, 2, "L", False,  "")

        pdf.set_y(pdf.get_y()+20)
        pdf.set_fill_color(228, 234, 236)
        pdf.rect(pdf.get_x(), pdf.get_y(), 210, 10, "F")
        
        pdf.set_font('Arial', 'B', 16)
        pdf.set_fill_color(240, 241, 242)
        pdf.rect(pdf.get_x(), pdf.get_y()+10, 210, 30, "F")
        pdf.cell(40, 10, f'Caracteristicas:', 0, 1, "L", False,  "")

        pdf.set_font('Arial', '', 14)
        pdf.set_x(pdf.get_x()+5)
        pdf.cell(40, 10, f'Cuartos:  {self.house.rooms}', 0, 2, "L", False,  "")
        pdf.cell(40, 10, f' Baños:    {self.house.bathrooms}', 0, 2, "L", False,  "")



        output:str = pdf.output(f'Casa_{self.house.id}.pdf', 'S')
        
        return [output, ""]
