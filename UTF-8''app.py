import gradio as gr
import math

class NumberSystemConverter:
    def __init__(self):
        self.hex2 = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
        self.hex1 = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
        self.s = "ABCDEF"
        self.number = "0123456789"
    
    def support(self, string1, num2):
        if num2 == 1 or num2 == 6 or num2 == 17 or num2 == 18 or num2 == 9 or num2 == 10:
            rad = 2
        elif num2 == 2 or num2 == 4 or num2 == 7 or num2 == 19 or num2 == 11 or num2 == 22:
            rad = 8
        elif num2 == 3 or num2 == 5 or num2 == 8 or num2 == 20 or num2 == 21 or num2 == 12:
            rad = 16
        else:
            return None, None, None
        
        sepernum = str(string1).split('.')
        inti = sepernum[0]
        deci = sepernum[1] if len(sepernum) > 1 else "0"
        return rad, inti, deci
    
    def DtoBOH(self, string1, n):
        stri = strd = ""
        r, i, d = self.support(string1, n)
        if r is None:
            return "Wrong input"
        
        d = "." + d
        dl = len(d)
        if dl < 5:
            dl = 5
        d = float(d)
        i = int(i)
        b = True
        
        while b:
            rem = i % r
            if rem >= 10:
                rem = self.hex1[str(rem)]
            stri = str(rem) + stri
            i = i // r
            if i < r:
                b = False
        
        if not i == 0:
            stri = str(i) + stri
        
        for k in range(0, dl):
            d = d * r
            sepernum1 = str(d).split('.')
            i = int(sepernum1[0])
            d = str(sepernum1[1])
            d = "." + d
            d = float(d)
            if i >= 10:
                i = self.hex1[str(i)]
            strd = strd + str(i)
        
        finalstr = stri + "." + strd
        return finalstr
    
    def OHBtoD(self, string1, n):
        numi = numd = numf = 0
        r, i, d = self.support(string1, n)
        if r is None:
            return "Wrong input"
        
        il = len(i)
        dl = len(d)
        j = il - 1
        
        for k in range(0, il):
            if i[k] in self.s:
                alpha = int(self.hex2[i[k]])
            elif i[k] in self.number:
                alpha = int(i[k])
            else:
                return "Wrong input"
            numi = alpha * (pow(r, j)) + numi
            j -= 1
        
        for k in range(0, dl):
            if d[k] in self.s:
                dalpha = int(self.hex2[d[k]])
            elif d[k] in self.number:
                dalpha = int(d[k])
            else:
                return "Wrong input"
            numd = dalpha * (pow(r, -(k + 1))) + numd
        
        numf = numi + numd
        return str(numf)
    
    def OHtoB(self, string1, n):
        strd = self.OHBtoD(string1, n)
        if strd == "Wrong input":
            return strd
        strh = self.DtoBOH(strd, n + 10)
        return strh
    
    def convert_number(self, conversion_type, input_number):
        try:
            # Add .0 if no decimal point
            if "." not in input_number:
                input_number = input_number + ".0"
            
            conversion_map = {
                "Decimal to Binary": 1,
                "Decimal to Octal": 2,
                "Decimal to Hexadecimal": 3,
                "Octal to Decimal": 4,
                "Hexadecimal to Decimal": 5,
                "Binary to Decimal": 6,
                "Octal to Binary": 7,
                "Hexadecimal to Binary": 8,
                "Binary to Octal": 9,
                "Binary to Hexadecimal": 10,
                "Octal to Hexadecimal": 11,
                "Hexadecimal to Octal": 12
            }
            
            num1 = conversion_map.get(conversion_type)
            if num1 is None:
                return "Invalid conversion type"
            
            if num1 <= 3:
                finalstr = str(self.DtoBOH(input_number, num1))
            elif num1 <= 6:
                finalstr = str(self.OHBtoD(input_number, num1))
            elif num1 <= 12:
                finalstr = str(self.OHtoB(input_number, num1))
            else:
                return "Wrong input"
            
            # Clean up trailing zeros
            if ".00000" in finalstr:
                finalstr = finalstr.split('.')[0]
            elif finalstr.endswith('.0'):
                finalstr = finalstr[:-2]
            
            return finalstr
            
        except Exception as e:
            return f"Error: {str(e)}"

# Initialize converter
converter = NumberSystemConverter()

# Create Gradio interface
def number_converter_interface(conversion_type, input_number):
    if not input_number.strip():
        return "Please enter a number to convert"
    
    result = converter.convert_number(conversion_type, input_number.strip().upper())
    return result

# Define the Gradio interface
iface = gr.Interface(
    fn=number_converter_interface,
    inputs=[
        gr.Dropdown(
            choices=[
                "Decimal to Binary",
                "Decimal to Octal", 
                "Decimal to Hexadecimal",
                "Octal to Decimal",
                "Hexadecimal to Decimal",
                "Binary to Decimal",
                "Octal to Binary",
                "Hexadecimal to Binary",
                "Binary to Octal",
                "Binary to Hexadecimal",
                "Octal to Hexadecimal",
                "Hexadecimal to Octal"
            ],
            label="Conversion Type",
            value="Decimal to Binary"
        ),
        gr.Textbox(
            label="Input Number",
            placeholder="Enter the number to convert (e.g., 123, 1010, FF, 777)",
            lines=1
        )
    ],
    outputs=gr.Textbox(label="Converted Result", lines=2),
    title="🔢 Number System Converter",
    description="Convert numbers between different number systems: Binary, Octal, Decimal, and Hexadecimal",
    examples=[
        ["Decimal to Binary", "123"],
        ["Decimal to Hexadecimal", "255"],
        ["Binary to Decimal", "1010"],
        ["Hexadecimal to Decimal", "FF"],
        ["Octal to Binary", "777"],
        ["Binary to Hexadecimal", "11111111"]
    ],
    theme="default"
)

# Launch the app
if __name__ == "__main__":
    iface.launch()