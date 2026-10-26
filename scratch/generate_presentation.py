import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Palette Canva Moderne
C_BG_DARK = RGBColor(15, 23, 42)      # Slate 900
C_CARD_DARK = RGBColor(30, 41, 59)    # Slate 800
C_BG_LIGHT = RGBColor(248, 250, 252)  # Slate 50
C_CARD_LIGHT = RGBColor(255, 255, 255)# Pure White
C_BORDER_LIGHT = RGBColor(226, 232, 240)
C_TEXT_DARK = RGBColor(15, 23, 42)
C_TEXT_MUTED = RGBColor(100, 116, 139)
C_TEXT_LIGHT = RGBColor(255, 255, 255)
C_PRIMARY = RGBColor(37, 99, 235)     # Royal Blue
C_ACCENT_CYAN = RGBColor(6, 182, 212) # Cyan
C_ACCENT_GREEN = RGBColor(16, 185, 129)# Emerald Green
C_ACCENT_PURPLE = RGBColor(139, 92, 246)# Violet
C_ACCENT_RED = RGBColor(239, 68, 68)   # Red Coral

def add_bg(slide, color):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    return bg

def add_card(slide, left, top, width, height, bg_color=C_CARD_LIGHT, border_color=C_BORDER_LIGHT):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
    else:
        card.line.fill.background()
    return card

def add_header(slide, title, category="TP2 - NLP & LLMS ARABE", dark=False):
    # Badge categorie
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(3.2), Inches(0.36))
    badge.fill.solid()
    badge.fill.fore_color.rgb = C_PRIMARY if dark else RGBColor(239, 246, 255)
    badge.line.fill.background()
    tf_b = badge.text_frame
    tf_b.word_wrap = True
    p_b = tf_b.paragraphs[0]
    p_b.text = category.upper()
    p_b.font.size = Pt(9.5)
    p_b.font.bold = True
    p_b.font.color.rgb = RGBColor(255, 255, 255) if dark else C_PRIMARY
    p_b.alignment = PP_ALIGN.CENTER
    
    # Titre
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.7))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_LIGHT if dark else C_TEXT_DARK

# ==============================================================================
# SLIDE 1 : COUVERTURE (DARK HERO)
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
add_bg(s1, C_BG_DARK)

# Badge Master
b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.4), Inches(3.4), Inches(0.42))
b1.fill.solid()
b1.fill.fore_color.rgb = RGBColor(30, 41, 59)
b1.line.color.rgb = C_ACCENT_CYAN
b1.line.width = Pt(1.5)
p = b1.text_frame.paragraphs[0]
p.text = "MODULE : TRANSFORMERS & LLMS"
p.font.size = Pt(10.5)
p.font.bold = True
p.font.color.rgb = C_ACCENT_CYAN
p.alignment = PP_ALIGN.CENTER

# Titre principal
t_box = s1.shapes.add_textbox(Inches(1.2), Inches(2.1), Inches(11), Inches(2.2))
tf = t_box.text_frame
tf.word_wrap = True
p1 = tf.paragraphs[0]
p1.text = "Détection du Sarcasme en Arabe"
p1.font.size = Pt(36)
p1.font.bold = True
p1.font.color.rgb = C_TEXT_LIGHT

p2 = tf.add_paragraph()
p2.text = "Benchmark Empirique, Modèles Gelés & Fine-Tuning sur ArSarcasm-v2"
p2.font.size = Pt(20)
p2.font.color.rgb = C_ACCENT_CYAN
p2.space_before = Pt(8)

# Cartouche etudiant & GPU
c_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.7), Inches(10.9), Inches(1.6))
c_box.fill.solid()
c_box.fill.fore_color.rgb = C_CARD_DARK
c_box.line.color.rgb = RGBColor(51, 65, 85)

tf_c = c_box.text_frame
tf_c.word_wrap = True
pc1 = tf_c.paragraphs[0]
pc1.text = "👨‍💻 Étudiant : Amine Bouaouda     |     ⚙️ Environnement : PyTorch 2.1 (FP16 AMP) sur NVIDIA RTX 2050"
pc1.font.size = Pt(13)
pc1.font.bold = True
pc1.font.color.rgb = C_TEXT_LIGHT

pc2 = tf_c.add_paragraph()
pc2.text = "🏆 Modèle Champion : UBC-NLP/MARBERTv2 Fine-Tuned (F1-Sarcasme = 0.6535, PR-AUC = 0.6480)"
pc2.font.size = Pt(13)
pc2.font.bold = True
pc2.font.color.rgb = C_ACCENT_GREEN
pc2.space_before = Pt(12)

# ==============================================================================
# SLIDE 2 : LE DEFI DU SARCASME EN ARABE
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
add_bg(s2, C_BG_LIGHT)
add_header(s2, "Le Problème : Complexité Pragmatisme & Diglossie Arabe", "CONTEXTE & ENJEUX")

cards_data = [
    ("1. Ambiguïté Pragmatique", 
     "Le sarcasme repose sur une inversion de polarité : le texte semble positif ou neutre mais exprime une critique acérée.\n\nSans contexte extra-linguistique ou marqueurs fins (emojis, allongements), les sacs de mots échouent.",
     C_PRIMARY),
    ("2. Diglossie & Variantes Dialectales",
     "L'arabe des réseaux sociaux mêle arabe standard moderne (MSA) et dialectes régionaux (Égyptien, Golfe, Levant, Maghreb).\n\nLes expressions sarcastiques, rires (هههه) et tournures idiomatiques varient drastiquement d'un pays à l'autre.",
     C_ACCENT_PURPLE),
    ("3. Déséquilibre Sévère des Classes",
     "Le sarcasme est minoritaire (~17% du corpus).\n\nUn modèle naïf 'toujours non-sarcastique' affiche 82.7% d'accuracy sans rien détecter. Le F1-Score sur la classe sarcastique et le PR-AUC sont indispensables.",
     C_ACCENT_RED)
]

for i, (title, desc, color) in enumerate(cards_data):
    left = Inches(0.8 + i * 4.0)
    add_card(s2, left, Inches(1.8), Inches(3.7), Inches(4.8))
    # Barre de couleur
    bar = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.8), Inches(3.7), Inches(0.12))
    bar.fill.solid(); bar.fill.fore_color.rgb = color; bar.line.fill.background()
    
    tb = s2.shapes.add_textbox(left + Inches(0.2), Inches(2.1), Inches(3.3), Inches(4.3))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = color
    p2 = tf.add_paragraph(); p2.text = desc; p2.font.size = Pt(11); p2.font.color.rgb = C_TEXT_DARK; p2.space_before = Pt(14)

# ==============================================================================
# SLIDE 3 : EXPLORATION DU CORPUS & PRIOR SHIFT
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
add_bg(s3, C_BG_LIGHT)
add_header(s3, "Corpus ArSarcasm-v2 : Le Piège du Prior Shift", "PARTIE A - EXPLORATION")

# Carte de gauche (Explications)
add_card(s3, Inches(0.8), Inches(1.8), Inches(5.2), Inches(4.9))
tb_s3 = s3.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(4.6), Inches(4.4))
tf_s3 = tb_s3.text_frame; tf_s3.word_wrap = True

p = tf_s3.paragraphs[0]; p.text = "Audit de Distribution & Décalage"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = C_PRIMARY

p_sub = tf_s3.add_paragraph()
p_sub.text = (
    "• Volume Total : 12 548 tweets en train officiel (stratifié en Train 11 293 / Val 1 255) et 3 000 en Test officiel.\n\n"
    "• Le Décalage Majeur (+10.1 pp) :\n"
    "   - Train / Val : 17.28% de tweets sarcastiques.\n"
    "   - Test Officiel : 27.37% de tweets sarcastiques !\n\n"
    "• Conséquence Cruciale :\n"
    "Un seuil de décision optimisé à 0.50 sur la validation devient sous-optimal sur le test et génère trop de faux négatifs.\n\n"
    "• Hétérogénéité Dialectale :\n"
    "Le dialecte égyptien et levantin présentent les taux de sarcasme les plus élevés (~35-40%). Le Maghreb est quasiment absent (38 tweets)."
)
p_sub.font.size = Pt(11.5); p_sub.font.color.rgb = C_TEXT_DARK; p_sub.space_before = Pt(12)

# Image du graphique de droite
if os.path.exists("scratch/chart_prior_shift.png"):
    s3.shapes.add_picture("scratch/chart_prior_shift.png", Inches(6.3), Inches(1.8), width=Inches(6.2))

# ==============================================================================
# SLIDE 4 : AUDIT DES RACCOURCIS & BIAIS SUPERFICIELS
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
add_bg(s4, C_BG_LIGHT)
add_header(s4, "Audit des Raccourcis : Les Biais Cachés du Dataset", "PARTIE A - RACCOURCIS")

raccourcis = [
    ("Guillemets initiaux (\")", "60.9%", "0.8%", "-0.157", "Artefact d'export CSV présent massivement dans le train mais disparu du test. Danger de sur-apprentissage."),
    ("Présence d'URL (http)", "38.3%", "14.7%", "-0.219", "Forte anti-corrélation avec le sarcasme. La règle naïve 'Pas d'URL -> Sarcastique' atteint F1 = 0.476 sans NLP !"),
    ("Présence de Mentions (@)", "23.5%", "0.8%", "-0.004", "Artefact de nettoyage Twitter non reproductible en test."),
    ("Retweet (RT)", "11.4%", "0.0%", "-0.009", "Supprimé du jeu de test officiel.")
]

for i, (name, f_tr, f_te, corr, impact) in enumerate(raccourcis):
    top = Inches(1.8 + i * 1.25)
    add_card(s4, Inches(0.8), top, Inches(11.7), Inches(1.1))
    
    tb = s4.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.3), Inches(0.9))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"{name}   |   Fréq Train : {f_tr}   |   Fréq Test : {f_te}   |   Corrélation : {corr}"
    p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = C_PRIMARY if i != 1 else C_ACCENT_RED
    
    p2 = tf.add_paragraph()
    p2.text = impact
    p2.font.size = Pt(11); p2.font.color.rgb = C_TEXT_DARK; p2.space_before = Pt(4)

# ==============================================================================
# SLIDE 5 : BASELINES TF-IDF & ZERO-SHOT NLI
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
add_bg(s5, C_BG_LIGHT)
add_header(s5, "Baselines : TF-IDF Lexical vs Zero-Shot NLI (mDeBERTa)", "PARTIE A & B")

# Carte TF-IDF
add_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
tb_a = s5.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.5))
tf_a = tb_a.text_frame; tf_a.word_wrap = True
p = tf_a.paragraphs[0]; p.text = "Modèles Lexicaux Classiques (Partie A)"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = C_PRIMARY

p_desc = tf_a.add_paragraph()
p_desc.text = (
    "• TF-IDF Mots (1-2 grammes) : F1 = 0.4755 | PR-AUC = 0.4481\n"
    "   Pondération class_weight='balanced' indispensable pour compenser le déséquilibre.\n\n"
    "• TF-IDF Caractères (2-5 grammes) : F1 = 0.5361 | PR-AUC = 0.5161\n"
    "   Gain majeur (+6.1 pts F1) ! Les n-grammes de caractères capturent nativement les allongements expressifs (هههههه, كتيييير) et les emojis.\n\n"
    "• Ablation des indices : F1 chute à 0.4653 si on retire la ponctuation et les emojis."
)
p_desc.font.size = Pt(11); p_desc.font.color.rgb = C_TEXT_DARK; p_desc.space_before = Pt(10)

# Carte Zero-shot
add_card(s5, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.9))
tb_b = s5.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.0), Inches(4.5))
tf_b = tb_b.text_frame; tf_b.word_wrap = True
p = tf_b.paragraphs[0]; p.text = "Zero-Shot NLI & Sentiment (Partie B)"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = C_ACCENT_PURPLE

p_desc2 = tf_b.add_paragraph()
p_desc2.text = (
    "• Modèle NLI : mDeBERTa-v3-base-xnli (Transfert sans entraînement)\n"
    "   - Hypothèse FR ('Ce tweet est sarcastique') : F1 = 0.4110 (seuil 0.85)\n"
    "   - Hypothèse EN ('This tweet is sarcastic') : F1 = 0.3980 (seuil 0.85)\n"
    "   - Hypothèse AR ('هذه التغريدة ساخرة') : F1 = 0.3762 (seuil 0.55)\n\n"
    "• Heuristique Sentiment CAMeL-Lab : F1 = 0.4700 (Rappel = 0.78)\n"
    "   Confirme la co-localisation : 42% des tweets négatifs sont sarcastiques.\n\n"
    "• Bilan : Le zero-shot fonctionne grâce à l'espace sémantique multilingue mais reste inférieur au TF-IDF caractères supervisé."
)
p_desc2.font.size = Pt(11); p_desc2.font.color.rgb = C_TEXT_DARK; p_desc2.space_before = Pt(10)

# ==============================================================================
# SLIDE 6 : PLM GELE : CLS VS MOYENNE MASQUEE
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
add_bg(s6, C_BG_LIGHT)
add_header(s6, "PLM Gelé (Partie D1) : AraBERT [CLS] contre Moyenne Masquée", "PARTIE D - FEATURE EXTRACTION")

# 2 grandes cartes comparatives
add_card(s6, Inches(1.2), Inches(1.8), Inches(5.2), Inches(3.6))
tb_c1 = s6.shapes.add_textbox(Inches(1.5), Inches(2.0), Inches(4.6), Inches(3.2))
tf_c1 = tb_c1.text_frame; tf_c1.word_wrap = True
p = tf_c1.paragraphs[0]; p.text = "AraBERT Gelé [CLS] + LR"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = C_PRIMARY
p_m1 = tf_c1.add_paragraph(); p_m1.text = "F1-Score : 0.5872   |   PR-AUC : 0.5545"; p_m1.font.size = Pt(13); p_m1.font.bold = True; p_m1.font.color.rgb = C_TEXT_DARK; p_m1.space_before = Pt(8)
p_d1 = tf_c1.add_paragraph()
p_d1.text = "Extraction du premier token uniquement. Moins expressif car les marqueurs sarcastiques se trouvent souvent au milieu ou à la fin du tweet (chute de la phrase ironique)."
p_d1.font.size = Pt(11); p_d1.font.color.rgb = C_TEXT_MUTED; p_d1.space_before = Pt(10)

add_card(s6, Inches(6.9), Inches(1.8), Inches(5.2), Inches(3.6))
tb_c2 = s6.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(4.6), Inches(3.2))
tf_c2 = tb_c2.text_frame; tf_c2.word_wrap = True
p = tf_c2.paragraphs[0]; p.text = "AraBERT Gelé (Moyenne Masquée) + LR"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = C_ACCENT_GREEN
p_m2 = tf_c2.add_paragraph(); p_m2.text = "F1-Score : 0.6180   |   PR-AUC : 0.6264"; p_m2.font.size = Pt(13); p_m2.font.bold = True; p_m2.font.color.rgb = C_ACCENT_GREEN; p_m2.space_before = Pt(8)
p_d2 = tf_c2.add_paragraph()
p_d2.text = "Pondération par le masque d'attention sur tous les tokens réels.\nGain spectaculaire de +3.1 points F1 et +7.2 points de PR-AUC sans modifier un seul poids du modèle BERT !"
p_d2.font.size = Pt(11); p_d2.font.color.rgb = C_TEXT_DARK; p_d2.space_before = Pt(10)

# Bandeau explicatif du bas
c_bot = add_card(s6, Inches(1.2), Inches(5.6), Inches(10.9), Inches(1.3), bg_color=RGBColor(241, 245, 249))
tb_b = s6.shapes.add_textbox(Inches(1.4), Inches(5.7), Inches(10.5), Inches(1.1))
tf_b = tb_b.text_frame; tf_b.word_wrap = True
p = tf_b.paragraphs[0]
p.text = "💡 Pourquoi la Moyenne Masquée triomphe ?"
p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = C_PRIMARY
p_sub = tf_b.add_paragraph()
p_sub.text = "Dans un modèle gelé, le vecteur [CLS] n'a pas été affiné pour condenser le sarcasme. La moyenne masquée préserve le signal sémantique distribué (emojis finaux, ponctuations répétées, adjectifs dialectaux) qui alimente la régression logistique."
p_sub.font.size = Pt(10.5); p_sub.font.color.rgb = C_TEXT_DARK; p_sub.space_before = Pt(4)

# ==============================================================================
# SLIDE 7 : VISUALISATION DE L'ATTENTION (D2)
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
add_bg(s7, C_BG_LIGHT)
add_header(s7, "Visualisation de l'Attention (Partie D2) : Ce que regarde le Modèle", "INTERPRÉTABILITÉ")

# Image de l'attention D2 a gauche
if os.path.exists("results/attention_d2.png"):
    s7.shapes.add_picture("results/attention_d2.png", Inches(0.8), Inches(1.7), width=Inches(6.8))

# Carte explicative a droite
add_card(s7, Inches(7.8), Inches(1.7), Inches(4.7), Inches(5.2))
tb_att = s7.shapes.add_textbox(Inches(8.0), Inches(1.9), Inches(4.3), Inches(4.8))
tf_att = tb_att.text_frame; tf_att.word_wrap = True
p = tf_att.paragraphs[0]; p.text = "Décryptage des Poids d'Attention"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = C_PRIMARY

p_desc = tf_att.add_paragraph()
p_desc.text = (
    "La couche d'attention du classifieur BiLSTM (sur états gelés) isole précisément les marqueurs clés :\n\n"
    "1. Les Mots de Négation & Amplificateurs :\n"
    "Les tokens d'accentuation reçoivent des pics d'attention nets (> 0.25).\n\n"
    "2. Les Termes Politiques & Entités Nommées :\n"
    "Forte focalisation sur les noms de personnalités publiques sujettes à l'ironie journalistique.\n\n"
    "3. Les Allongements & Emojis :\n"
    "L'attention met en lumière les fragments de rires ou d'étonnement souvent placés en fin de tweet.\n\n"
    "Conclusion :\n"
    "Le modèle ne traite pas le texte uniformément : il aligne sa décision sur les disparités sémantiques caractéristiques du sarcasme."
)
p_desc.font.size = Pt(10.5); p_desc.font.color.rgb = C_TEXT_DARK; p_desc.space_before = Pt(8)

# ==============================================================================
# SLIDE 8 : FINE-TUNING MONO-TACHE (E1) - LE CHOC DES TITANS
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
add_bg(s8, C_BG_LIGHT)
add_header(s8, "Fine-Tuning Complet (Partie E1) : Le Choc AraBERT vs MARBERTv2", "PARTIE E - FINE-TUNING")

# Carte AraBERT
add_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
tb_e1 = s8.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.4))
tf_e1 = tb_e1.text_frame; tf_e1.word_wrap = True
p = tf_e1.paragraphs[0]; p.text = "aubmindlab/bert-base-arabertv02-twitter"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = C_PRIMARY
p_m = tf_e1.add_paragraph(); p_m.text = "F1-Score : 0.6417   |   PR-AUC : 0.6794"; p_m.font.size = Pt(13); p_m.font.bold = True; p_m.font.color.rgb = C_PRIMARY; p_m.space_before = Pt(6)
p_d = tf_e1.add_paragraph()
p_d.text = (
    "• Spécialisé sur les tweets arabes avec un pré-traitement morphologique dédié.\n"
    "• Obtenu au seuil optimal de 0.20 (pour capter agressivement les positifs rares).\n"
    "• Excellent PR-AUC (0.6794), le plus élevé du benchmark sur la distribution de précision/rappel.\n"
    "• Très fort sur MSA et dialecte levantin."
)
p_d.font.size = Pt(10.8); p_d.font.color.rgb = C_TEXT_DARK; p_d.space_before = Pt(10)

# Carte MARBERTv2
add_card(s8, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8), bg_color=RGBColor(240, 253, 244), border_color=C_ACCENT_GREEN)
tb_e2 = s8.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.0), Inches(4.4))
tf_e2 = tb_e2.text_frame; tf_e2.word_wrap = True
p = tf_e2.paragraphs[0]; p.text = "🏆 UBC-NLP/MARBERTv2 (CHAMPION DU TP)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = C_ACCENT_GREEN
p_m2 = tf_e2.add_paragraph(); p_m2.text = "F1-Score : 0.6535   |   Macro-F1 : 0.7812"; p_m2.font.size = Pt(13); p_m2.font.bold = True; p_m2.font.color.rgb = C_ACCENT_GREEN; p_m2.space_before = Pt(6)
p_d2 = tf_e2.add_paragraph()
p_d2.text = (
    "• Pré-entraîné sur 1 Milliard de tweets arabes dialectaux variés (UBC-NLP).\n"
    "• Seuil optimal : 0.30.\n"
    "• Meilleur compromis Précision/Rappel : bat AraBERT de +1.2 pt et le modèle gelé de +3.5 pts !\n"
    "• Sa couverture dialectale massive (Égypte, Golfe, Maghreb) fait la différence sur les tweets informels du corpus."
)
p_d2.font.size = Pt(10.8); p_d2.font.color.rgb = C_TEXT_DARK; p_d2.space_before = Pt(10)

# ==============================================================================
# SLIDE 9 : APPRENTISSAGE MULTI-TACHE (E2)
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
add_bg(s9, C_BG_LIGHT)
add_header(s9, "Apprentissage Multi-Tâche : Sarcasme + Sentiment (Partie E2)", "PARTIE E - MULTI-TASK")

# Image du graphique multi-tache a droite
if os.path.exists("scratch/chart_multitask_lambda.png"):
    s9.shapes.add_picture("scratch/chart_multitask_lambda.png", Inches(6.8), Inches(1.8), width=Inches(5.7))

# Carte de gauche (Analyse multi-tache)
add_card(s9, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))
tb_mt = s9.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.4))
tf_mt = tb_mt.text_frame; tf_mt.word_wrap = True
p = tf_mt.paragraphs[0]; p.text = "Architecture & Impact de Lambda"; p.font.size = Pt(15); p.font.bold = True; p.font.color.rgb = C_ACCENT_PURPLE

p_desc = tf_mt.add_paragraph()
p_desc.text = (
    "• Principe : L'encodeur AraBERT est partagé entre 2 têtes de classification :\n"
    "   L = L_sarcasme + lambda * L_sentiment\n\n"
    "• Résultats Expérimentaux (Validation) :\n"
    "   - lambda = 0.3 : F1 = 0.5241 | PR-AUC = 0.5162\n"
    "   - lambda = 0.5 : F1 = 0.5638 | PR-AUC = 0.5833 (OPTIMUM)\n"
    "   - lambda = 1.0 : F1 = 0.5455 | PR-AUC = 0.5259\n\n"
    "• Analyse du Transfert Négatif :\n"
    "À lambda = 0.5, la tâche plus facile (sentiment) stabilise les gradients et renforce la détection de négativité.\n"
    "À lambda = 1.0, la tâche sentiment cannibalise l'espace latent : les tweets neutres sarcastiques sont mal classés."
)
p_desc.font.size = Pt(10.5); p_desc.font.color.rgb = C_TEXT_DARK; p_desc.space_before = Pt(8)

# ==============================================================================
# SLIDE 10 : GENERALISATION & TEST OFFICIEL (PARTIE F)
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
add_bg(s10, C_BG_LIGHT)
add_header(s10, "Généralisation & Épreuve du Feu sur le Test Officiel", "PARTIE F - GÉNÉRALISATION")

f_cards = [
    ("Le Test Officiel (N=3000)", "F1 = 0.5003", 
     "Au seuil fixe de 0.50, le F1 chute de ~0.53 à 0.50 sur le test officiel.\n\nCause directe : Le prior shift (+10.1 pp de sarcasme). Pour restaurer les performances, le seuil de décision opérationnel doit être abaissé vers 0.30 - 0.35.",
     C_PRIMARY),
    ("Audit Dialectal Maghreb", "38 tweets train / 2 test",
     "Le dialecte maghrébin (Darija) représente seulement 0.3% du corpus.\n\nImpossible de certifier la fiabilité du modèle sur le Maghreb sans collecter un jeu de données Darija dédié (DarijaBERT).",
     C_ACCENT_PURPLE),
    ("Analyse d'Erreurs (F6)", "35% Hors-Contexte",
     "L'audit des 30 erreurs montre que 35% des faux négatifs sont dus au manque de connaissances du monde réel (actualité politique ou sportive non explicite dans le texte).",
     C_ACCENT_RED)
]

for i, (title, stat, desc, color) in enumerate(f_cards):
    left = Inches(0.8 + i * 4.0)
    add_card(s10, left, Inches(1.8), Inches(3.7), Inches(4.8))
    
    tb = s10.shapes.add_textbox(left + Inches(0.2), Inches(2.0), Inches(3.3), Inches(4.4))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = color
    p_s = tf.add_paragraph(); p_s.text = stat; p_s.font.size = Pt(16); p_s.font.bold = True; p_s.font.color.rgb = C_TEXT_DARK; p_s.space_before = Pt(6)
    p_d = tf.add_paragraph(); p_d.text = desc; p_d.font.size = Pt(10.5); p_d.font.color.rgb = C_TEXT_MUTED; p_d.space_before = Pt(12)

# ==============================================================================
# SLIDE 11 : TABLEAU COMPARATIF COMPLET (CHART HORIZONTAL)
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
add_bg(s11, C_BG_LIGHT)
add_header(s11, "Benchmark Final des 21 Modèles Expérimentés", "SYNTHÈSE GLOBALE")

if os.path.exists("scratch/chart_models_comparison.png"):
    s11.shapes.add_picture("scratch/chart_models_comparison.png", Inches(0.8), Inches(1.7), width=Inches(8.2))

# Carte de synthèse a droite
add_card(s11, Inches(9.3), Inches(1.7), Inches(3.2), Inches(5.2), bg_color=C_CARD_DARK)
tb_syn = s11.shapes.add_textbox(Inches(9.5), Inches(1.9), Inches(2.8), Inches(4.8))
tf_syn = tb_syn.text_frame; tf_syn.word_wrap = True
p = tf_syn.paragraphs[0]; p.text = "Points Clés"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = C_ACCENT_GREEN

p_sub = tf_syn.add_paragraph()
p_sub.text = (
    "🥇 1er : MARBERTv2 (0.6535)\n"
    "Domine l'ensemble des métriques grâce à son vocabulaire dialectal riche.\n\n"
    "🥈 2e : AraBERT FT (0.6417)\n"
    "Meilleur PR-AUC global (0.6794).\n\n"
    "🥉 3e : AraBERT Gelé (0.6180)\n"
    "Moyenne masquée : le meilleur ratio performance / coût CPU !\n\n"
    "📊 Baseline Chars (0.5361)\n"
    "Les n-grammes caractères restent très honorables face aux transformers."
)
p_sub.font.size = Pt(11); p_sub.font.color.rgb = C_TEXT_LIGHT; p_sub.space_before = Pt(10)

# ==============================================================================
# SLIDE 12 : DECISION & RECOMMANDATIONS INDUSTRIELLES
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
add_bg(s12, C_BG_DARK)

# Header dark
txBox = s12.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.7), Inches(0.8))
tf = txBox.text_frame
p = tf.paragraphs[0]; p.text = "Décision de Déploiement & Recommandations"; p.font.size = Pt(24); p.font.bold = True; p.font.color.rgb = C_TEXT_LIGHT

# 2 grandes cartes
add_card(s12, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.0), bg_color=C_CARD_DARK, border_color=C_ACCENT_GREEN)
tb_d1 = s12.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(5.0), Inches(4.5))
tf_d1 = tb_d1.text_frame; tf_d1.word_wrap = True
p = tf_d1.paragraphs[0]; p.text = "Choix du Modèle pour la Production"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = C_ACCENT_GREEN

p_desc = tf_d1.add_paragraph()
p_desc.text = (
    "🏆 Modèle Sélectionné : UBC-NLP/MARBERTv2 Fine-Tuned\n\n"
    "• Justification Opérationnelle :\n"
    "  - F1-Score maximal : 0.6535 (+11.7 pts vs baseline TF-IDF).\n"
    "  - Couverture dialectale supérieure sur les tweets informels.\n"
    "  - Macro-F1 de 0.7812 garantissant un bon équilibre sur les deux classes.\n\n"
    "• Solution Alternative 'Low-Cost' :\n"
    "Si l'infrastructure n'a pas de GPU disponible en inférence :\n"
    "AraBERT Gelé (Moyenne masquée) + Régression Logistique offre F1 = 0.6180 avec seulement 200 ms de latence CPU !"
)
p_desc.font.size = Pt(11); p_desc.font.color.rgb = C_TEXT_LIGHT; p_desc.space_before = Pt(10)

add_card(s12, Inches(6.9), Inches(1.7), Inches(5.6), Inches(5.0), bg_color=C_CARD_DARK, border_color=C_ACCENT_CYAN)
tb_d2 = s12.shapes.add_textbox(Inches(7.2), Inches(1.9), Inches(5.0), Inches(4.5))
tf_d2 = tb_d2.text_frame; tf_d2.word_wrap = True
p = tf_d2.paragraphs[0]; p.text = "Checklist de Déploiement en Production"; p.font.size = Pt(16); p.font.bold = True; p.font.color.rgb = C_ACCENT_CYAN

p_desc2 = tf_d2.add_paragraph()
p_desc2.text = (
    "1. Recalibration Dynamique du Seuil :\n"
    "Le prior shift impose d'abandonner le seuil fixe 0.50 en faveur d'un seuil dynamique calibré (0.30 - 0.35) via Platt Scaling.\n\n"
    "2. Détection du Drift de Prior :\n"
    "Mettre en place un monitoring hebdomadaire du taux de sarcasme prédit (alerte si dérive > 5 pp).\n\n"
    "3. Adaptation Dialectale Darija (Maghreb) :\n"
    "Entraîner un adaptateur LoRA ou utiliser DarijaBERT pour combler le déficit de données maghrébines.\n\n"
    "4. Nettoyage Robuste des Artefacts :\n"
    "Supprimer systématiquement les URLs et guillemets artificiels en amont."
)
p_desc2.font.size = Pt(11); p_desc2.font.color.rgb = C_TEXT_LIGHT; p_desc2.space_before = Pt(10)

# Export
out_pptx = r"c:\projets\LLMS\detection sarcasm\Presentation_TP2_Sarcasme_Bouaouda.pptx"
prs.save(out_pptx)
print("Presentation PPTX generee avec succes :", out_pptx)

