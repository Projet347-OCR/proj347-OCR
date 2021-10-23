import pytesseract

custom_oem_psm_config = r'--oem 3 --psm 6'
# pytesseract.image_to_string(image, config=custom_oem_psm_config)

# Example of using pre-defined tesseract config file with options
cfg_filename = 'words'
# pytesseract.run_and_get_output(image, extension='txt', config=cfg_filename)