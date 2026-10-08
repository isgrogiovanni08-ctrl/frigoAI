from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="FrigoAI - Anti-Spreco", page_icon="🥗", layout="wide"
)

# Inizializzazione dello stato della dispensa
if "inventory" not in st.session_state:
  st.session_state.inventory = pd.DataFrame([
      {
          "Prodotto": "Latte Fresco",
          "Quantità": "1 L",
          "Scadenza": (datetime.now() + timedelta(days=1)).strftime(
              "%Y-%m-%d"
          ),
          "Categoria": "Latticini",
      },
      {
          "Prodotto": "Petto di Pollo",
          "Quantità": "500g",
          "Scadenza": (datetime.now() + timedelta(days=2)).strftime(
              "%Y-%m-%d"
          ),
          "Categoria": "Carne",
      },
      {
          "Prodotto": "Spinaci Freschi",
          "Quantità": "250g",
          "Scadenza": (datetime.now() + timedelta(days=0)).strftime(
              "%Y-%m-%d"
          ),
          "Categoria": "Verdura",
      },
      {
          "Prodotto": "Yogurt Greco",
          "Quantità": "2 pezzi",
          "Scadenza": (datetime.now() + timedelta(days=3)).strftime(
              "%Y-%m-%d"
          ),
          "Categoria": "Latticini",
      },
  ])

st.title("🥗 FrigoAI: Gestione Intelligente e Anti-Spreco")

# Tab di navigazione
tab1, tab2, tab3, tab4 = st.tabs(
    ["📦 Inventario Frigo", "📸 Scansiona (IA)", "🍳 Ricette", "🛒 Riordino Smart"]
)

with tab1:
  st.header("Il tuo inventario attuale")
  df = st.session_state.inventory

  # Evidenziazione scadenze imminenti
  def color_expiry(val):
    try:
      d = datetime.strptime(val, "%Y-%m-%d")
      diff = (d - datetime.now()).days
      if diff < 1:
        return "background-color: #ffcccc; color: black;"
      elif diff <= 2:
        return "background-color: #fff3cd; color: black;"
    except:
      pass
    return ""

  st.dataframe(df.style.map(color_expiry, subset=["Scadenza"]), use_container_width=True)
  
  if st.button("Aggiungi prodotto manuale"):
    st.info("Funzionalità di inserimento rapido attiva.")

with tab2:
  st.header("Visione Artificiale (Simulazione)")
  st.write("Carica la foto dello scontrino o l'interno del frigo:")
  uploaded_file = st.file_uploader(
      "Scegli un'immagine...", type=["jpg", "png", "jpeg"]
  )

  if uploaded_file is not None:
    st.image(uploaded_file, caption="Immagine caricata", use_column_width=True)
    with st.spinner("Analisi IA in corso (OCR & Riconoscimento oggetti)..."):
      # Simulazione aggiunta automatica
      new_item = pd.DataFrame([{
          "Prodotto": "Mozzarella di Bufala",
          "Quantità": "1 pezzo",
          "Scadenza": (datetime.now() + timedelta(days=2)).strftime(
              "%Y-%m-%d"
          ),
          "Categoria": "Latticini",
      }])
      st.session_state.inventory = pd.concat(
          [st.session_state.inventory, new_item], ignore_index=True
      )
    st.success(
        "Scansione completata! Rilevato: **Mozzarella di Bufala** aggiunto alla"
        " dispensa."
    )

with tab3:
  st.header("Ricette Salva-Frigo personalizzate")
  st.write(
      "Basate sugli ingredienti che scadono prima (Spinaci, Latte, Pollo):"
  )

  st.subheader("🍲 Pollo agli spinaci cremosi")
  st.markdown("""
    * **Tempo:** 15 minuti
    * **Difficoltà:** Facile
    * **Ingredienti usati:** Petto di pollo, Spinaci freschi, Latte fresco (per la cremosità).
    * **Procedimento:** Rosola il pollo in padella, aggiungi gli spinaci freschi e sfuma con un goccio di latte per creare una salsa densa.
    """)
  if st.button("Cucina questa ricetta"):
    st.success(
        "Ottimo! Gli ingredienti sono stati scalati automaticamente dal tuo"
        " frigo."
    )

with tab4:
  st.header("Riordino E-commerce Intelligente")
  st.write("Prodotti terminati o in esaurimento pronti per il carrello:")

  cart_items = ["Latte Fresco", "Uova", "Pane in cassetta"]
  for item in cart_items:
    st.checkbox(f"Aggiungi {item} al carrello", value=True)

  if st.button("Invia ordine al supermercato partner"):
    st.success(
        "Carrello sincronizzato con successo con il tuo e-commerce di fiducia!"
    )
