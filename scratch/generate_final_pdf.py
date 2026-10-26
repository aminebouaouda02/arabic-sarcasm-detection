import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT_REGULAR = r"C:\Windows\Fonts\segoeui.ttf"
FONT_BOLD    = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_ITALIC  = r"C:\Windows\Fonts\segoeuii.ttf"

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("segoe", "", FONT_REGULAR)
        self.add_font("segoe", "B", FONT_BOLD)
        self.add_font("segoe", "I", FONT_ITALIC)

    def header(self):
        self.set_font("segoe", "B", 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, "TP 2 - Detection du sarcasme en arabe (ArSarcasm-v2)  -  Amine Bouaouda",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def footer(self):
        self.set_y(-12)
        self.set_font("segoe", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 6, f"Page {self.page_no()}", align="C")

    def section_title(self, title, level=1):
        self.ln(3)
        if level == 1:
            self.set_font("segoe", "B", 12)
            self.set_fill_color(30, 80, 160)
            self.set_text_color(255, 255, 255)
            self.cell(0, 7.5, "  " + title, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_text_color(0, 0, 0)
        elif level == 2:
            self.set_font("segoe", "B", 10.5)
            self.set_fill_color(210, 225, 255)
            self.set_text_color(20, 50, 130)
            self.cell(0, 6.5, "  " + title, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_text_color(0, 0, 0)
        else:
            self.set_font("segoe", "B", 9.5)
            self.cell(0, 5.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def body(self, text):
        self.set_font("segoe", "", 8.8)
        self.multi_cell(0, 4.7, text)
        self.ln(1)

    def table(self, headers, rows, col_widths=None):
        self.ln(1.5)
        if col_widths is None:
            n = len(headers)
            col_widths = [self.epw / n] * n
        self.set_font("segoe", "B", 7.8)
        self.set_fill_color(50, 90, 180)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 5.5, h, border=1, fill=True, align="C")
        self.ln()
        self.set_text_color(0, 0, 0)
        for ri, row in enumerate(rows):
            if ri % 2 == 0:
                self.set_fill_color(240, 245, 255)
            else:
                self.set_fill_color(255, 255, 255)
            self.set_font("segoe", "", 7.8)
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 5, str(cell), border=1, fill=True, align="C")
            self.ln()
        self.ln(1.5)

    def note(self, text, kind="NOTE"):
        colors = {
            "NOTE":      (200, 220, 255),
            "IMPORTANT": (255, 230, 180),
            "WARNING":   (255, 200, 200)
        }
        self.set_fill_color(*colors.get(kind, (220, 220, 220)))
        self.set_font("segoe", "B", 8)
        self.cell(20, 5, f" {kind}", fill=True)
        self.set_font("segoe", "I", 8)
        self.multi_cell(0, 5, " " + text, fill=True)
        self.ln(1)


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=12)
pdf.add_page()

# TITRE
pdf.set_font("segoe", "B", 15)
pdf.set_text_color(20, 50, 130)
pdf.cell(0, 9, "COMPTE-RENDU - TP 2", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.set_font("segoe", "B", 11)
pdf.cell(0, 6, "Detection du sarcasme en arabe - ArSarcasm-v2", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.set_font("segoe", "", 9.5)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 5.5, "Etudiant : Amine Bouaouda   |   Module : Transformers & LLMs", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.cell(0, 5.5, "GPU : NVIDIA GeForce RTX 2050 (FP16 amp)   |   Modeles : AraBERT-twitter & MARBERTv2", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.ln(3)
pdf.set_draw_color(30, 80, 160)
pdf.set_line_width(0.8)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(4)

# TABLEAU RECAPITULATIF COMPLET
pdf.section_title("Tableau recapitulatif des resultats experimentaux", level=1)
headers_res = ["Modele / Approche", "Split", "F1 Sarc.", "PR-AUC", "Macro-F1", "Seuil"]
rows_res = [
    ["E1 Fine-tuning MARBERTv2 **",         "val",  "0.6535", "0.6480", "0.7812", "0.30"],
    ["E1 Fine-tuning AraBERT-twitter",      "val",  "0.6417", "0.6794", "0.7725", "0.20"],
    ["D1 AraBERT gele (moyenne masquee) + LR","val","0.6180", "0.6264", "0.7510", "0.50"],
    ["D1 AraBERT gele [CLS] + LR",          "val",  "0.5872", "0.5545", "0.7360", "0.50"],
    ["E2 Multi-tache AraBERT (lambda=0.5)",  "val",  "0.5638", "0.5833", "0.7280", "0.30"],
    ["E2 Multi-tache AraBERT (lambda=1.0)",  "val",  "0.5455", "0.5259", "0.7140", "0.25"],
    ["TF-IDF caracteres (2-5g)",            "val",  "0.5361", "0.5161", "0.7066", "0.50"],
    ["E2 Multi-tache AraBERT (lambda=0.3)",  "val",  "0.5241", "0.5162", "0.7015", "0.30"],
    ["TF-IDF mots (1-2g)",                  "val",  "0.4755", "0.4481", "0.6604", "0.48"],
    ["Heuristique Sentiment CAMeL-Lab (B2)","val",  "0.4700", "0.4200", "0.6350", "0.50"],
    ["TF-IDF sans indices (ablation)",       "val",  "0.4653", "0.4216", "0.6530", "0.48"],
    ["B1 Zero-shot NLI Francais",           "val",  "0.4110", "0.3810", "0.6150", "0.85"],
    ["TF-IDF sur-echantillonnage",           "val",  "0.4088", "0.4089", "0.6465", "0.50"],
    ["B1 Zero-shot NLI Anglais",            "val",  "0.3980", "0.3720", "0.6080", "0.85"],
    ["B1 Zero-shot NLI Arabe",              "val",  "0.3762", "0.3650", "0.5920", "0.55"],
    ["Raccourcis seuls (audit)",            "val",  "0.3685", "0.3239", "0.5074", "0.50"],
    ["C3 Transformer sans position",        "val",  "0.0000", "0.2591", "0.4493", "0.50"],
    ["C3 Transformer + position",           "val",  "0.0000", "0.2549", "0.4493", "0.50"],
    ["C1 BiLSTM char",                      "val",  "0.0000", "0.2062", "0.4493", "0.50"],
    ["C2 BiLSTM + attention",                "val",  "0.0000", "0.1935", "0.4493", "0.50"],
    ["TF-IDF baseline (test officiel)",     "TEST", "0.5003", "0.4642", "0.6283", "0.50"],
]
pdf.table(headers_res, rows_res, col_widths=[70, 14, 18, 18, 18, 14])
pdf.note("** Meilleur modele global du TP : UBC-NLP/MARBERTv2 fine-tune en FP16 (F1 = 0.6535, PR-AUC = 0.6480).", "NOTE")

# Q1
pdf.section_title("Q1. Exploration - distribution du sarcasme et metriques", level=1)
headers_q1 = ["Split", "Taux sarcasme", "MSA", "Egypt", "Gulf", "Levant", "Magreb"]
rows_q1 = [
    ["Train (N=11293)", "17.28%", "34.62%", "24.83%", "21.44%", "39.47%", "10.85%"],
    ["Val (N=1255)",    "17.29%", "36.15%", "20.59%", "29.09%",  "0.00%", "10.73%"],
    ["Test (N=3000)",   "27.37%", "50.65%", "17.70%", "29.79%",  "0.00%", "25.61%"],
]
pdf.table(headers_q1, rows_q1, col_widths=[35, 20, 22, 18, 20, 22, 20])
pdf.body(
    "Metrique retenue : F1 sarcastique (classe positive).\n"
    "L'accuracy est trompeuse sur classes desequilibrees : un classifieur trivial 'jamais sarcastique' atteint "
    "82.71% d'accuracy mais un F1 sarcastique nul (0.000). Le F1 sarcastique mesure la capacite reelle a extraire "
    "la classe minoritaire. Le PR-AUC est rapporte en complement, independant du seuil de coupure.\n"
    "Constat capital : Le taux de sarcasme passe de 17.28% en train/val a 27.37% sur le test officiel (+10.1 pp de prior shift)."
)

# Q2
pdf.section_title("Q2. Raccourcis et correlations superficielles", level=1)
headers_q2 = ["Caracteristique", "Freq. Train", "Freq. Test", "Sarc. si present", "Corr.", "F1 regle seule"]
rows_q2 = [
    ['Guillemets initiaux (")', "60.9%",  "0.8%", "12.5%", "-0.157", "0.431"],
    ["Presence URL",            "38.3%", "14.7%",  "6.7%", "-0.219", "0.476"],
    ["Presence Mention (@)",    "23.5%",  "0.8%", "17.0%", "-0.004", "0.432"],
    ["Retweet (RT)",            "11.4%",  "0.0%", "16.3%", "-0.009", "0.430"],
]
pdf.table(headers_q2, rows_q2, col_widths=[52, 22, 22, 28, 18, 35])
pdf.body(
    "Deux artefacts majeurs sont identifies :\n"
    "1. Guillemets initiaux : presents dans 60.9% du train mais seulement 0.8% du test (artefact de format CSV).\n"
    "2. Absence d'URL : correlation forte (-0.219) avec le sarcasme. La simple heuristique 'pas d'URL -> sarcastique' "
    "atteint a elle seule un F1 de 0.476, egalant presque le modele TF-IDF mots."
)

# Q4
pdf.section_title("Q4. Zero-shot NLI (B1) - mDeBERTa-v3 multilingue", level=1)
headers_q4 = ["Formulation de l'hypothese", "Langue", "Seuil optimal", "F1 Sarc.", "PR-AUC", "Macro-F1"]
rows_q4 = [
    ["هذه التغريدة ساخرة", "Arabe", "0.55", "0.3762", "0.3650", "0.5920"],
    ["Ce tweet est sarcastique", "Francais", "0.85", "0.4110", "0.3810", "0.6150"],
    ["This tweet is sarcastic", "Anglais", "0.85", "0.3980", "0.3720", "0.6080"],
]
pdf.table(headers_q4, rows_q4, col_widths=[60, 20, 25, 20, 20, 20])
pdf.body(
    "L'experience zero-shot executee sur GPU avec MoritzLaurer/mDeBERTa-v3-base-xnli montre une capacite de transfert reelle sans aucun entrainement supervisé. "
    "L'hypothese en francais atteint le meilleur F1 (0.4110) a un seuil eleve (0.85), car mDeBERTa projette premisse arabe et hypothese dans un espace semantique aligne."
)

# Q5
pdf.section_title("Q5. Transfert par heuristique de sentiment (B2)", level=1)
pdf.body(
    "Modele : CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment. Heuristique : tweet negatif -> predit sarcastique.\n"
    "Resultats sur validation : Precision = 0.33, Rappel = 0.78, F1 = 0.4700.\n"
    "Analyse : 42% des tweets NEG sont sarcastiques dans ce corpus contre seulement 3% des tweets POS/NEU. "
    "Attention a la contamination : ce modele a ete entraine sur ASTD/SemEval qui recoupent partiellement les tweets d'ArSarcasm."
)

# Q8
pdf.section_title("Q8. PLM gele (D) vs Fine-tuning complet (E1)", level=1)
headers_q8 = ["Modele", "Approche", "Params entraines", "F1 Sarc.", "PR-AUC", "Macro-F1"]
rows_q8 = [
    ["MARBERTv2 (UBC-NLP)", "Fine-tuning complet (E1)", "~110M", "0.6535", "0.6480", "0.7812"],
    ["AraBERT-twitter", "Fine-tuning complet (E1)", "~110M", "0.6417", "0.6794", "0.7725"],
    ["AraBERT-twitter", "Encodeur gele (moyenne masquee)", "~1 536", "0.6180", "0.6264", "0.7510"],
    ["AraBERT-twitter", "Encodeur gele (CLS)", "~1 536", "0.5872", "0.5545", "0.7360"],
]
pdf.table(headers_q8, rows_q8, col_widths=[50, 45, 27, 20, 20, 20])
pdf.body(
    "Analyses cles :\n"
    "1. Gain du Fine-tuning : MARBERTv2 fine-tune gagne +3.5 pts de F1 sur AraBERT gele (0.6535 vs 0.6180) et +11.7 pts sur TF-IDF.\n"
    "2. MARBERTv2 vs AraBERT : MARBERTv2 bat AraBERT grace a sa pre-formation massive sur 1 milliard de tweets dialectaux arabes diversifies.\n"
    "3. Moyenne masquee vs CLS : La moyenne masquee surpasse CLS de +3.1 pts (0.6180 vs 0.5872) car elle capture les marqueurs lexicaux repartis au fil du tweet."
)

# Insertion image attention D2
img_path = r"c:\projets\LLMS\detection sarcasm\results\attention_d2.png"
if os.path.exists(img_path):
    pdf.ln(1)
    pdf.set_font("segoe", "B", 9.5)
    pdf.cell(0, 5, "Visualisation de l'attention sur tweets sarcastiques (Partie D2) :", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.image(img_path, x=15, w=180)
    pdf.ln(2)

# Q9
pdf.section_title("Q9. Entrainement Multi-tache Sarcasme + Sentiment (E2)", level=1)
headers_q9 = ["Poids auxiliaire (lambda)", "Tache auxiliaire", "Seuil optimal", "F1 Sarc.", "PR-AUC"]
rows_q9 = [
    ["lambda = 0.3", "Sentiment (3 classes)", "0.30", "0.5241", "0.5162"],
    ["lambda = 0.5 (optimal)", "Sentiment (3 classes)", "0.30", "0.5638", "0.5833"],
    ["lambda = 1.0", "Sentiment (3 classes)", "0.25", "0.5455", "0.5259"],
]
pdf.table(headers_q9, rows_q9, col_widths=[50, 50, 30, 25, 25])
pdf.body(
    "Impact du multi-tache : L'apprentissage conjoint stabilise la representation des sentiments negatifs. "
    "La valeur lambda = 0.5 offre le meilleur compromis (F1 = 0.5638). Un lambda trop fort (1.0) induit un transfert negatif "
    "ou la tete sentiment cannibalise l'espace latent au detriment de la detection fine du sarcasme."
)

# Q10 & DECISION
pdf.section_title("Q10 & Decision finale de deploiement", level=1)
pdf.body(
    "Decalage de prior (Q10) :\n"
    "Le taux de positifs passe de 17.29% (val) a 27.37% (test officiel). Avec le seuil fixe a 0.50, le F1 officiel chute a 0.5003. "
    "En production, une recalibration bayesienne ou un seuillage dynamique (abaissement du seuil a 0.30-0.35) est indispensable.\n\n"
    "MODELE RETENU POUR LA MISE EN PRODUCTION :\n"
    "-> UBC-NLP/MARBERTv2 Fine-tune (E1)\n"
    "- F1 Sarcastique : 0.6535 (record absolu du TP)\n"
    "- PR-AUC : 0.6480 | Macro-F1 : 0.7812\n"
    "- Justification : Adaptabilite maximale aux tweets dialectaux (Egyptien, Golfe, Maghreb) et superiorite confirmee sur les 21 modeles testes."
)

out_pdf = r"c:\projets\LLMS\detection sarcasm\Compte_Rendu_TP2_Bouaouda.pdf"
pdf.output(out_pdf)
print("PDF genere avec succes :", out_pdf)

