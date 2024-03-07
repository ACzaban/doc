
# po 8 taskow od 1 do końca
    tasks_1_8 = lista_taski(json_file, 0, 8, 1)
    modified_1_8 = replace_paragraphs_with_random_text(document_path, tasks_1_8, '01/Mar/23 - 30/Apr/23', 'March 2023',80)
    modified_1_8.save("_modified_1_8.docx")
    print("First document generated successfully.")
    
    tasks_8_16 = lista_taski(json_file, 8, 16, 1)
    modified_8_16 = replace_paragraphs_with_random_text(document_path, tasks_8_16,'01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_8_16.save("_modified_8_16.docx")
    print("Second document generated successfully.")

    tasks_16_24 = lista_taski(json_file, 16, 24, 1)
    modified_16_24 = replace_paragraphs_with_random_text(document_path, tasks_16_24,'01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_16_24.save("_modified_16_24.docx")
    print("Second document generated successfully.")
        
    tasks_24_32 = lista_taski(json_file, 24, 32, 1)
    modified_24_32 = replace_paragraphs_with_random_text(document_path, tasks_24_32,'01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_24_32.save("_modified_24_32.docx")
    print("Second document generated successfully.")

    tasks_32_40 = lista_taski(json_file, 32, 40, 1)
    modified_32_40 = replace_paragraphs_with_random_text(document_path, tasks_32_40,'01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_32_40.save("_modified_32_40.docx")
    print("Second document generated successfully.")

    tasks_40_48 = lista_taski(json_file, 40, 48, 1)
    modified_40_48 = replace_paragraphs_with_random_text(document_path, tasks_40_48,'01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_40_48.save("_modified_40_48.docx")
    print("Second document generated successfully.")


# co 8 taskow od dolu 


    tasks_step_32_to_4 = lista_taski(json_file, 32, 4, -7)
    tasks_from_48 = lista_taski(json_file, 48, 0, -7)
    tasks_combined = tasks_step_32_to_4 + tasks_from_48
    tasks_combined_first_8 = tasks_combined[:7]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_combined_first_8, '01/Mar/23 - 30/Apr/23', 'March 2023',76)
    modified_doc_step.save("_modified_step.docx")
    print("2 document generated successfully.")

#co 8 od góry
    tasks_step_32_to_4 = lista_taski(json_file, 32, 50, 8)
    tasks_from_48 = lista_taski(json_file, 0, 50, 8)
    tasks_combined = tasks_step_32_to_4 + tasks_from_48
    tasks_combined_8_up = tasks_combined[:7]
    modified_doc_step_8 = replace_paragraphs_with_random_text(document_path, tasks_combined_8_up, '01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_doc_step_8.save("_modified_step_8.docx")
    print("Second document generated successfully.")


    tasks_step_8 = lista_taski(json_file, 0, 46, 8)
    modified_doc_step_8 = replace_paragraphs_with_random_text(document_path, tasks_step_8, '01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_doc_step_8.save("_modified_step_8.docx")
    print("Second document generated successfully.")
  








  # od 8 do konca itd...
    tasks_8_to_50 = lista_taski(json_file, 7, 50, 7)
    tasks_1_50 = lista_taski(json_file, 1, 50, 7)
    tasks_combined_8_50 = tasks_8_to_50 + tasks_1_50
    tasks_8_1 = tasks_combined_8_50[:7]
    modified_doc_step_8 = replace_paragraphs_with_random_text(document_path, tasks_8_1, '01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_doc_step_8.save("1.docx")
    print("Second document generated successfully.")

    tasks_43_0 = lista_taski(json_file, 42, 0, -7)
    tasks_42_0 = lista_taski(json_file, 41, 0, -7)
    tasks_combined_43_0 = tasks_43_0 + tasks_42_0
    tasks_43_42 = tasks_combined_43_0[:7]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_43_42, '01/Mar/23 - 30/Apr/23', 'March 2023',76)
    modified_doc_step.save("2.docx")
    print("2 document generated successfully.")



#od 7 do konca itd
    tasks_7_to_50 = lista_taski(json_file, 6, 50, 7)
    tasks_1_50 = lista_taski(json_file, 1, 50, 7)
    tasks_combined_7_50 = tasks_7_to_50 + tasks_1_50
    tasks_7_1 = tasks_combined_7_50[:7]
    modified_doc_step_7 = replace_paragraphs_with_random_text(document_path, tasks_7_1, '01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_doc_step_7.save("1.docx")
    print("Second document generated successfully.")

    tasks_6_to_50 = lista_taski(json_file, 5, 50, 7)
    tasks_2_50 = lista_taski(json_file, 2, 50, 7)
    tasks_combined_6_50 = tasks_6_to_50 + tasks_2_50
    tasks_6_2 = tasks_combined_6_50[:8]
    modified_doc_step_6 = replace_paragraphs_with_random_text(document_path, tasks_6_2, '01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_doc_step_6.save("3.docx")
    print("Second document generated successfully.")

    tasks_5_to_50 = lista_taski(json_file, 4, 50, 7)
    tasks_3_50 = lista_taski(json_file, 3, 50, 7)
    tasks_combined_5_50 = tasks_5_to_50 + tasks_5_to_50
    tasks_5_3 = tasks_combined_5_50[:8]
    modified_doc_step_5 = replace_paragraphs_with_random_text(document_path, tasks_5_3, '01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_doc_step_5.save("3.docx")
    print("Second document generated successfully.")

    tasks_14_50 = lista_taski(json_file, 13, 50, 7)
    tasks_10_50 = lista_taski(json_file, 10, 50, 7)
    tasks_combined_14_50 = tasks_14_50 + tasks_10_50
    tasks_14_10 = tasks_combined_14_50[:8]
    modified_doc_step_5 = replace_paragraphs_with_random_text(document_path, tasks_14_10, '01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_doc_step_5.save("3.docx")
    print("Second document generated successfully.")

    tasks_13_50 = lista_taski(json_file, 12, 50, 7)
    tasks_11_50 = lista_taski(json_file, 11, 50, 7)
    tasks_combined_13_50 = tasks_13_50 + tasks_11_50
    tasks_13_11 = tasks_combined_13_50[:8]
    modified_doc_step_5 = replace_paragraphs_with_random_text(document_path, tasks_13_11, '01/Mar/23 - 30/Apr/23', 'March 2023',85)
    modified_doc_step_5.save("3.docx")
    print("Second document generated successfully.")


    tasks_42_0 = lista_taski(json_file, 41, 0, -7)
    tasks_41_0 = lista_taski(json_file, 40, 0, -7)
    tasks_combined_42_0 = tasks_42_0 + tasks_41_0
    tasks_42_41 = tasks_combined_42_0[:7]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_42_41, '01/Mar/23 - 30/Apr/23', 'March 2023',76)
    modified_doc_step.save("2.docx")
    print("2 document generated successfully.")

    tasks_40_0 = lista_taski(json_file, 39, 0, -7)
    tasks_38_0 = lista_taski(json_file, 38, 0, -7)
    tasks_combined_40_0 = tasks_40_0 + tasks_38_0
    tasks_40_38 = tasks_combined_41_0[:6]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_40_38, '01/Mar/23 - 30/Apr/23', 'March 2023',76)
    modified_doc_step.save("2.docx")
    print("2 document generated successfully.")

    tasks_29_0 = lista_taski(json_file, 28, 0, -7)
    tasks_23_0 = lista_taski(json_file, 23, 0, -7)
    tasks_combined_29_0 = tasks_29_0 + tasks_23_0
    tasks_29_23 = tasks_combined_29_0[:6]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_29_23, '01/Mar/23 - 30/Apr/23', 'March 2023',76)
    modified_doc_step.save("2.docx")
    print("2 document generated successfully.")

    tasks_28_0 = lista_taski(json_file, 27, 0, -7)
    tasks_22_0 = lista_taski(json_file, 22, 0, -7)
    tasks_combined_28_0 = tasks_28_0 + tasks_22_0
    tasks_28_22 = tasks_combined_28_0[:6]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_28_22, '01/Mar/23 - 30/Apr/23', 'March 2023',76)
    modified_doc_step.save("2.docx")
    print("2 document generated successfully.")

 
 #początek- koniec

    tasks_1_8 = lista_taski(json_file, 0, 8, 1)
    modified_1_8 = replace_paragraphs_with_random_text(document_path, tasks_1_8, '01/Feb/23 - 28/Feb/23', 'Ferbruary 2023',80)
    modified_1_8.save("_modified_1_8.docx")
    print("First document generated successfully.")
    
    tasks_8_16 = lista_taski(json_file, 8, 16, 1)
    modified_8_16 = replace_paragraphs_with_random_text(document_path, tasks_8_16,'01/Mar/23 - 31/Mar/23', 'March 2023',80)
    modified_8_16.save("_modified_8_16.docx")
    print("Second document generated successfully.")

    tasks_16_24 = lista_taski(json_file, 16, 24, 1)
    modified_16_24 = replace_paragraphs_with_random_text(document_path, tasks_16_24,'01/Apr/23 - 30/Apr/23', 'April 2023',80)
    modified_16_24.save("_modified_16_24.docx")
    print("Second document generated successfully.")
        
    tasks_24_32 = lista_taski(json_file, 24, 32, 1)
    modified_24_32 = replace_paragraphs_with_random_text(document_path, tasks_24_32,'01/May/23 - 31/May/23', 'May 2023',80)
    modified_24_32.save("_modified_24_32.docx")
    print("Second document generated successfully.")

    tasks_32_40 = lista_taski(json_file, 32, 40, 1)
    modified_32_40 = replace_paragraphs_with_random_text(document_path, tasks_32_40,'01/June/23 - 30/June/23', 'June 2023',80)
    modified_32_40.save("_modified_32_40.docx")
    print("Second document generated successfully.")

    tasks_40_48 = lista_taski(json_file, 40, 48, 1)
    modified_40_48 = replace_paragraphs_with_random_text(document_path, tasks_40_48,'01/July/23 - 31/July/23', 'July 2023',80)
    modified_40_48.save("_modified_40_48.docx")
    print("Second document generated successfully.")


# pocz koniec od dolu

    tasks_40_48 = lista_taski(json_file, 40, 48, 1)
    modified_40_48 = replace_paragraphs_with_random_text(document_path, tasks_40_48,'01/June/23 - 30/June/23', 'June 2023',93)
    modified_40_48.save("A. Ilyk 06.2023.docx")
    print("Second document generated successfully.")

    tasks_32_40 = lista_taski(json_file, 32, 40, 1)
    modified_32_40 = replace_paragraphs_with_random_text(document_path, tasks_32_40,'01/May/23 - 31/May/23', 'May 2023',87)
    modified_32_40.save("A. Ilyk 05.2023.docx")
    print("Second document generated successfully.")

    tasks_24_32 = lista_taski(json_file, 24, 32, 1)
    modified_24_32 = replace_paragraphs_with_random_text(document_path, tasks_24_32,'01/Apr/23 - 30/Apr/23', 'April 2023',87)
    modified_24_32.save("A. Ilyk 04.2023.docx")
    print("Second document generated successfully.")

    tasks_16_24 = lista_taski(json_file, 16, 24, 1)
    modified_16_24 = replace_paragraphs_with_random_text(document_path, tasks_16_24,'01/Mar/23 - 31/Mar/23', 'March 2023',87)
    modified_16_24.save("A. Ilyk 03.2023.docx")
    print("Second document generated successfully.")
        
    tasks_8_16 = lista_taski(json_file, 8, 16, 1)
    modified_8_16 = replace_paragraphs_with_random_text(document_path, tasks_8_16,'01/Jan/23 - 31/Jan/23', 'January 2023',88)
    modified_8_16.save("A. Ilyk 01.2023.docx")
    print("Second document generated successfully.")

    tasks_1_8 = lista_taski(json_file, 0, 8, 1)
    modified_1_8 = replace_paragraphs_with_random_text(document_path, tasks_1_8, '01/Dec/22 - 31/Dec/22', 'December 2022',87)
    modified_1_8.save("A. Ilyk 12.2022.docx")
    print("First document generated successfully.")
    

#co osiem od gory i od dolu
    tasks_0_50 = lista_taski(json_file, 0, 50, 7)
    modified_0_50 = replace_paragraphs_with_random_text(document_path, tasks_0_50, '01/Aug/23 - 31/Aug/23', 'August 2023',80)
    modified_0_50.save("R. Gajda 02.2023.docx")
    print("Second document generated successfully.")

    tasks_50_0 = lista_taski(json_file, 50, 0, -7)
    modified_50_0 = replace_paragraphs_with_random_text(document_path, tasks_50_0, '01/Sept/23 - 30/Sept/23', 'September 2023',80)
    modified_50_0.save("R. Gajda 03.2023.docx")
    print("2 document generated successfully.")





#przydkład od listopada

 tasks_1_8 = lista_taski(json_file, 0, 8, 1)
    modified_1_8 = replace_paragraphs_with_random_text(document_path, tasks_1_8, '01/Nov/22 - 30/Nov/22', 'November 2022',80)
    modified_1_8.save("D. Kamola 11.2022.docx")
    print("First document generated successfully.")

    tasks_8_to_50 = lista_taski(json_file, 7, 50, 7)
    tasks_1_50 = lista_taski(json_file, 1, 50, 7)
    tasks_combined_8_50 = tasks_8_to_50 + tasks_1_50
    tasks_8_1 = tasks_combined_8_50[:8]
    modified_doc_step_8 = replace_paragraphs_with_random_text(document_path, tasks_8_1, '01/Dec/22 - 31/Dec/22', 'December 2022',80)
    modified_doc_step_8.save("D. Kamola 12.2022.docx")
    print("Second document generated successfully.")

    tasks_6_to_50 = lista_taski(json_file, 5, 50, 7)
    tasks_2_50 = lista_taski(json_file, 2, 50, 7)
    tasks_combined_6_50 = tasks_6_to_50 + tasks_2_50
    tasks_6_2 = tasks_combined_6_50[:8]
    modified_doc_step_6 = replace_paragraphs_with_random_text(document_path, tasks_6_2, '01/Jan/23 - 31/Jan/23', 'January 2023',80)
    modified_doc_step_6.save("D. Kamola 01.2023.docx")
    print("Second document generated successfully.")

    tasks_5_to_50 = lista_taski(json_file, 4, 50, 7)
    tasks_3_50 = lista_taski(json_file, 3, 50, 7)
    tasks_combined_5_50 = tasks_5_to_50 + tasks_5_to_50
    tasks_5_3 = tasks_combined_5_50[:7]
    modified_doc_step_5 = replace_paragraphs_with_random_text(document_path, tasks_5_3, '01/Feb/23 - 28/February/23', 'February 2023',80)
    modified_doc_step_5.save("D. Kamola 02.2023.docx")
    print("Second document generated successfully.")
    
    tasks_13_50 = lista_taski(json_file, 12, 50, 7)
    tasks_11_50 = lista_taski(json_file, 11, 50, 7)
    tasks_combined_13_50 = tasks_13_50 + tasks_11_50
    tasks_13_11 = tasks_combined_13_50[:8]
    modified_doc_step_5 = replace_paragraphs_with_random_text(document_path, tasks_13_11, '01/Mar/23 - 31/Mar/23', 'March 2023',85)
    modified_doc_step_5.save("D. Kamola 03.2023.docx")
    print("Second document generated successfully.")

    tasks_7_to_50 = lista_taski(json_file, 6, 50, 7)
    tasks_1_50 = lista_taski(json_file, 1, 50, 7)
    tasks_combined_7_50 = tasks_7_to_50 + tasks_1_50
    tasks_7_1 = tasks_combined_7_50[:7]
    modified_doc_step_7 = replace_paragraphs_with_random_text(document_path, tasks_7_1, '01/Apr/23 - 30/Apr/23', 'April 2023',80)
    modified_doc_step_7.save("D. Kamola 04.2023.docx")
    print("Second document generated successfully.")

    tasks_29_0 = lista_taski(json_file, 28, 0, -7)
    tasks_23_0 = lista_taski(json_file, 23, 0, -7)
    tasks_combined_29_0 = tasks_29_0 + tasks_23_0
    tasks_29_23 = tasks_combined_29_0[:6]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_29_23, '01/May/23 - 31/May/23', 'May 2023',76)
    modified_doc_step.save("D. Kamola 05.2023.docx")
    print("2 document generated successfully.")
        
    tasks_24_32 = lista_taski(json_file, 24, 32, 1)
    modified_24_32 = replace_paragraphs_with_random_text(document_path, tasks_24_32,'01/June/23 - 30/June/23', 'June 2023',80)
    modified_24_32.save("D. Kamola 06.2023.docx")
    print("Second document generated successfully.")

    tasks_14_50 = lista_taski(json_file, 13, 50, 7)
    tasks_10_50 = lista_taski(json_file, 10, 50, 7)
    tasks_combined_14_50 = tasks_14_50 + tasks_10_50
    tasks_14_10 = tasks_combined_14_50[:8]
    modified_doc_step_5 = replace_paragraphs_with_random_text(document_path, tasks_14_10, '01/July/23 - 31/July/23', 'July 2023',85)
    modified_doc_step_5.save("D. Kamola 07.2023.docx")
    print("Second document generated successfully.")


    tasks_28_0 = lista_taski(json_file, 27, 0, -7)
    tasks_22_0 = lista_taski(json_file, 22, 0, -7)
    tasks_combined_28_0 = tasks_28_0 + tasks_22_0
    tasks_28_22 = tasks_combined_28_0[:8]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_28_22, '01/Aug/23 - 31/Aug/23', 'August 2023',80)
    modified_doc_step.save("D. Kamola 08.2023.docx")
    print("2 document generated successfully.")


    tasks_0_50 = lista_taski(json_file, 0, 50, 7)
    modified_0_50 = replace_paragraphs_with_random_text(document_path, tasks_0_50, '01/Sept/23 - 30/Sept/23', 'September 2023',80)
    modified_0_50.save("D. Kamola 09.2023.docx")
    print("Second document generated successfully.")

    tasks_7_to_50 = lista_taski(json_file, 6, 50, 7)
    tasks_1_50 = lista_taski(json_file, 1, 50, 7)
    tasks_combined_7_50 = tasks_7_to_50 + tasks_1_50
    tasks_7_1 = tasks_combined_7_50[:7]
    modified_doc_step_7 = replace_paragraphs_with_random_text(document_path, tasks_7_1, '01/Oct/23 - 31/Oct/23', 'October 2023',80)
    modified_doc_step_7.save("D. Kamola 10.2023.docx")
    print("Second document generated successfully.")


    tasks_42_0 = lista_taski(json_file, 41, 0, -7)
    tasks_38_0 = lista_taski(json_file, 38, 0, -7)
    tasks_combined_42_0 = tasks_42_0 + tasks_38_0
    tasks_42_38 = tasks_combined_42_0[:8]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_42_38, '01/Nov/23 - 30/Nov/23', 'November 2023',80)
    modified_doc_step.save("D. Kamola 11.2023.docx")
    print("2 document generated successfully.")

    tasks_41_0 = lista_taski(json_file, 40, 0, -7)
    tasks_37_0 = lista_taski(json_file, 37, 0, -7)
    tasks_combined_41_0 = tasks_41_0 + tasks_37_0
    tasks_41_37 = tasks_combined_41_0[:8]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_41_37, '01/Dec/23 - 31/Dec/23', 'December 2023',80)
    modified_doc_step.save("D. Kamola 12.2023.docx")
    print("2 document generated successfully.")

    tasks_40_0 = lista_taski(json_file, 39, 0, -7)
    tasks_38_0 = lista_taski(json_file, 38, 0, -7)
    tasks_combined_40_0 = tasks_40_0 + tasks_38_0
    tasks_40_38 = tasks_combined_41_0[:7]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_40_38, '01/Jan/24 - 31/Jan/24', 'January 2024',80)
    modified_doc_step.save("D. Kamola 01.2024.docx")
    print("2 document generated successfully.")


    tasks_43_0 = lista_taski(json_file, 42, 0, -7)
    tasks_42_0 = lista_taski(json_file, 41, 0, -7)
    tasks_combined_43_0 = tasks_43_0 + tasks_42_0
    tasks_43_42 = tasks_combined_43_0[:7]
    modified_doc_step = replace_paragraphs_with_random_text(document_path, tasks_43_42, '01/Feb/24 - 29/Feb/24', 'February 2024',80)
    modified_doc_step.save("D. Kamola 02.2024.docx")
    print("2 document generated successfully.")


#przyklad 2
