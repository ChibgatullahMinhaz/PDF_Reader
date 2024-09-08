import PyPDF2

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            num_pages = len(pdf_reader.pages)
            print(f'Total Pages: {num_pages}')
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                print(f'\n--- Page {page_num + 1} ---\n')
                print(page.extract_text())
    except Exception as e:
        print(f"Error: {e}")


pdf_path = "Business Communication.pdf" 
read_pdf(pdf_path)
