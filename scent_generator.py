{\rtf1\ansi\ansicpg1252\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red38\green38\blue38;\red250\green249\blue246;}
{\*\expandedcolortbl;;\cssrgb\c20000\c20000\c20000;\cssrgb\c98431\c98039\c97255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\
\pard\pardeftab720\partightenfactor0

\f1 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import streamlit as st\cb1 \
\
\cb3 # Set up the app title and description\cb1 \
\cb3 st.title("Discover Your Signature Scent in *Stelo Vienas*")\cb1 \
\cb3 st.write("Follow the steps to reveal the unique scent that reflects your journey through *Stelo Vienas*.")\cb1 \
\
\cb3 # Step 1: Character Class Selection\cb1 \
\cb3 st.header("Step 1: Choose Your Character Class")\cb1 \
\cb3 character_class = st.selectbox(\cb1 \
\cb3 "Which character class resonates with you the most?",\cb1 \
\cb3 ("Mystic", "Scholar", "Warrior", "Adventurer")\cb1 \
\cb3 )\cb1 \
\
\cb3 # Step 2: Aroma Selection Based on Character Class\cb1 \
\cb3 st.header("Step 2: Select Your Aromas")\cb1 \
\cb3 if character_class == "Mystic":\cb1 \
\cb3 aroma = st.multiselect(\cb1 \
\cb3 "Select up to two aromas that resonate with your spirit:",\cb1 \
\cb3 ["Night Bloom", "Incense", "Herbal Mist"]\cb1 \
\cb3 )\cb1 \
\cb3 elif character_class == "Scholar":\cb1 \
\cb3 aroma = st.multiselect(\cb1 \
\cb3 "Select up to two aromas that speak of knowledge:",\cb1 \
\cb3 ["Leather", "Fresh Ink", "Sandalwood"]\cb1 \
\cb3 )\cb1 \
\cb3 elif character_class == "Warrior":\cb1 \
\cb3 aroma = st.multiselect(\cb1 \
\cb3 "Choose up to two aromas that fuel your courage:",\cb1 \
\cb3 ["Blood Orange", "Cedar", "Iron"]\cb1 \
\cb3 )\cb1 \
\cb3 else: # Adventurer\cb1 \
\cb3 aroma = st.multiselect(\cb1 \
\cb3 "Select up to two aromas that evoke adventure:",\cb1 \
\cb3 ["Wild Mint", "Ocean Mist", "Pine Resin"]\cb1 \
\cb3 )\cb1 \
\
\cb3 # Step 3: Display Outcome\cb1 \
\cb3 if st.button("Reveal Your Signature Scent"):\cb1 \
\cb3 if character_class == "Mystic" and set(aroma) == \{"Night Bloom", "Incense"\}:\cb1 \
\cb3 st.subheader("Veil of Midnight")\cb1 \
\cb3 st.write("A lingering scent of moonlit flowers and incense smoke, filling the air with whispers of secrets.")\cb1 \
\cb3 elif character_class == "Mystic" and set(aroma) == \{"Night Bloom", "Herbal Mist"\}:\cb1 \
\cb3 st.subheader("Twilight Grove")\cb1 \
\cb3 st.write("The gentle fragrance of herbs under a starlit sky, with hints of mystical blooms.")\cb1 \
\cb3 elif character_class == "Mystic" and set(aroma) == \{"Incense", "Herbal Mist"\}:\cb1 \
\cb3 st.subheader("Sacred Hearth")\cb1 \
\cb3 st.write("A blend of smoke and earth, evoking ancient rituals and hidden knowledge.")\cb1 \
\cb3 elif character_class == "Scholar" and set(aroma) == \{"Leather", "Fresh Ink"\}:\cb1 \
\cb3 st.subheader("The Quiet Archive")\cb1 \
\cb3 st.write("The scent of wisdom bound in leather and fresh ink, conjuring a sense of discovery and thought.")\cb1 \
\cb3 elif character_class == "Scholar" and set(aroma) == \{"Leather", "Sandalwood"\}:\cb1 \
\cb3 st.subheader("Timeless Study")\cb1 \
\cb3 st.write("A blend of warm sandalwood and worn leather, like a sanctuary of hidden knowledge.")\cb1 \
\cb3 elif character_class == "Scholar" and set(aroma) == \{"Fresh Ink", "Sandalwood"\}:\cb1 \
\cb3 st.subheader("Script of the Ages")\cb1 \
\cb3 st.write("A fragrance as sharp and grounded as ink on parchment, softened by the warmth of sandalwood.")\cb1 \
\cb3 elif character_class == "Warrior" and set(aroma) == \{"Blood Orange", "Cedar"\}:\cb1 \
\cb3 st.subheader("Vanguard\'92s Charge")\cb1 \
\cb3 st.write("The bright energy of citrus balanced with the earthy strength of cedar\'97a scent for those who lead.")\cb1 \
\cb3 elif character_class == "Warrior" and set(aroma) == \{"Blood Orange", "Iron"\}:\cb1 \
\cb3 st.subheader("Forge\'92s Edge")\cb1 \
\cb3 st.write("A sharp, invigorating fragrance of metal and citrus, like the spark of a warrior\'92s blade.")\cb1 \
\cb3 elif character_class == "Warrior" and set(aroma) == \{"Cedar", "Iron"\}:\cb1 \
\cb3 st.subheader("Ironwood Resolve")\cb1 \
\cb3 st.write("The grounded strength of cedar entwined with the metallic tang of iron, symbolizing resilience.")\cb1 \
\cb3 elif character_class == "Adventurer" and set(aroma) == \{"Wild Mint", "Ocean Mist"\}:\cb1 \
\cb3 st.subheader("Breeze of the Open")\cb1 \
\cb3 st.write("A crisp blend of mint and sea air, evoking freedom and discovery.")\cb1 \
\cb3 elif character_class == "Adventurer" and set(aroma) == \{"Wild Mint", "Pine Resin"\}:\cb1 \
\cb3 st.subheader("Forest Wanderer")\cb1 \
\cb3 st.write("A fragrance of fresh mint and pine, like a path through sunlit woods.")\cb1 \
\cb3 elif character_class == "Adventurer" and set(aroma) == \{"Ocean Mist", "Pine Resin"\}:\cb1 \
\cb3 st.subheader("Edge of the World")\cb1 \
\cb3 st.write("The earthy tang of pine with the cool embrace of the ocean, a call to distant horizons.")\cb1 \
\cb3 else:\cb1 \
\cb3 st.write("Please select up to two aromas to reveal your signature scent.")\cb1 \
}