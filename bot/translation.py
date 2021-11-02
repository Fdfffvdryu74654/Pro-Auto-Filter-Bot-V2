#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG @MRK_YT

class Translation(object):
    
    START_TEXT = """<b>ℍ𝕒𝕚🙋{}!!</b>

<b>𝕀 𝕒𝕞 𝕒 ℙ𝕣𝕠 𝔸𝕦𝕥𝕠𝔽𝕚𝕝𝕥𝕖𝕣𝔹𝕠𝕥 𝕍𝟚....😜</b>

<b>𝕄𝕒𝕜𝕖 𝕞𝕖 𝕒𝕟 𝕒𝕕𝕞𝕚𝕟 𝕗𝕠𝕣 𝕪𝕠𝕦𝕣 𝕘𝕣𝕠𝕦𝕡 𝕒𝕟𝕕 𝕔𝕙𝕒𝕟𝕟𝕖𝕝 𝕥𝕙𝕖𝕟 𝕔𝕠𝕟𝕟𝕖𝕔𝕥 𝕞𝕖....🎉</b>

<b>𝕃𝕠𝕠𝕜 𝕠𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝 𝕗𝕠𝕣 𝕓𝕠𝕥 𝕦𝕡𝕕𝕒𝕥𝕖𝕕.𝕜𝕖𝕖𝕡 𝕤𝕦𝕡𝕡𝕠𝕣𝕥𝕚𝕟𝕘🙏...</b>

<b>ℙ𝕝𝕖𝕒𝕤𝕖 𝕊𝕙𝕒𝕣𝕖 𝕥𝕙𝕚𝕤 𝕓𝕠𝕥 𝕒𝕟𝕕 𝕤𝕦𝕡𝕡𝕠𝕣𝕥 💘...</b>

<b>ℙ𝕣𝕖𝕤𝕤 /help 𝕥𝕠 𝕜𝕟𝕠𝕨 𝕒𝕓𝕠𝕦𝕥 𝕒𝕧𝕒𝕚𝕝𝕒𝕓𝕝𝕖 𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤😁</b>"""    
    
    HELP_TEXT = """
<b>🤡How To Use Me!🤡?</b>

<i>
-> 𝓐𝓭𝓭 𝓜𝓮 𝓣𝓸 𝓐𝓷𝔂 𝓖𝓻𝓸𝓾𝓹 𝓐𝓷𝓭 𝓜𝓪𝓴𝓮 𝓜𝓮 𝓐𝓭𝓶𝓲𝓷😎
-> 𝓐𝓭𝓭 𝓜𝓮 𝓣𝓸 𝓨𝓸𝓾𝓻 𝓓𝓮𝓼𝓲𝓻𝓮𝓭 𝓒𝓱𝓪𝓷𝓷𝓮𝓵😍
</i>

<b>Bot Commands (Works Only In Groups) :</b>

    -> <code>/add chat_id</code>
                OR                  - <b>𝕋𝕠 ℂ𝕠𝕟𝕟𝕖𝕔𝕥 𝔸 𝔾𝕣𝕠𝕦𝕡 𝕎𝕚𝕥𝕙 𝔸 ℂ𝕙𝕒𝕟𝕟𝕖𝕝😎(𝔹𝕠𝕥 𝕊𝕙𝕠𝕦𝕝𝕕 𝔹𝕖 𝔸𝕕𝕞𝕚𝕟 𝕎𝕚𝕥𝕙 𝔽𝕦𝕝𝕝 ℙ𝕣𝕖𝕧𝕚𝕝𝕒𝕘𝕖𝕤 𝕀𝕟 𝔹𝕠𝕥𝕙 𝔾𝕣𝕠𝕦𝕡 𝔸𝕟𝕕 ℂ𝕙𝕒𝕟𝕟𝕖𝕝)</b>
     <code>/add @Username</code>
     
    -> <code>/del chat_id</code>
                OR                  - <b>𝕋𝕠 𝕕𝕚𝕤𝕔𝕠𝕟𝕟𝕖𝕔𝕥 𝔸 𝔾𝕣𝕠𝕦𝕡 𝕎𝕚𝕥𝕙 𝔸 ℂ𝕙𝕒𝕟𝕟𝕖𝕝😎</b>
     <code>/del @Username</code>
     
    -> <code>/delall</code>  - <b>𝕋𝕙𝕚𝕤 ℂ𝕠𝕞𝕞𝕒𝕟𝕕 𝕎𝕚𝕝𝕝 𝔻𝕚𝕤𝕔𝕠𝕟𝕟𝕖𝕔𝕥 𝔸𝕝𝕝 ℂ𝕠𝕟𝕟𝕖𝕔𝕥𝕖𝕕 ℂ𝕙𝕒𝕟𝕟𝕖𝕝 𝕎𝕚𝕥𝕙 𝕋𝕙𝕖 𝔾𝕣𝕠𝕦𝕡 𝔸𝕟𝕕 𝔻𝕖𝕝𝕖𝕥𝕖𝕤 𝔸𝕝𝕝 𝕀𝕥𝕤 𝔽𝕚𝕝𝕖 𝔽𝕣𝕠𝕞 𝔻𝔹😎</b>
    
    -> <code>/settings</code> -  <b>𝕋𝕙𝕚𝕤 ℂ𝕠𝕞𝕞𝕒𝕟𝕕 𝕎𝕚𝕝𝕝 𝔻𝕚𝕤𝕡𝕝𝕒𝕪 𝕐𝕠𝕦 𝔸 𝕊𝕖𝕥𝕥𝕚𝕟𝕘𝕤 ℙ𝕒𝕟𝕟𝕖𝕝 𝕀𝕟𝕤𝕥𝕒𝕟𝕔𝕖 𝕎𝕙𝕚𝕔𝕙 ℂ𝕒𝕟 𝔹𝕖 𝕌𝕤𝕖𝕕 𝕋𝕠 𝕋𝕨𝕖𝕖𝕜 𝔹𝕠𝕥'𝕤 𝕊𝕖𝕥𝕥𝕚𝕟𝕘𝕤 𝔸𝕔𝕔𝕠𝕣𝕕𝕚𝕟𝕘𝕝𝕪😎</b>

            -> <code>Channel</code> - <b>𝔹𝕦𝕥𝕥𝕠𝕟 𝕎𝕚𝕝𝕝 𝕊𝕙𝕠𝕨 𝕐𝕠𝕦 𝔸𝕝𝕝 𝕋𝕙𝕖 ℂ𝕠𝕟𝕟𝕖𝕔𝕥𝕖𝕕 ℂ𝕙𝕒𝕥𝕤 𝕎𝕚𝕥𝕙 𝕋𝕙𝕖 𝔾𝕣𝕠𝕦𝕡 𝔸𝕟𝕕 𝕎𝕚𝕝𝕝 𝕊𝕙𝕠𝕨 𝔹𝕦𝕥𝕥𝕠𝕟𝕤 ℂ𝕠𝕣𝕣𝕖𝕤𝕡𝕟𝕕𝕚𝕟𝕘 𝕋𝕠 𝕋𝕙𝕖𝕣𝕖 𝕆𝕣𝕕𝕖𝕣 𝔽𝕠𝕣 𝔽𝕦𝕣𝕥𝕙𝕦𝕣 ℂ𝕠𝕟𝕥𝕣𝕠𝕝𝕤🤡</b>
            
            -> <code>Filter Types</code> - <b>𝔹𝕦𝕥𝕥𝕠𝕟 𝕎𝕚𝕝𝕝 ℍ𝕖𝕝𝕡𝕤 𝕐𝕠𝕦 𝕋𝕠 ℂ𝕙𝕒𝕟𝕘𝕖 ℕ𝕠. 𝕠𝕗 ℙ𝕒𝕘𝕖𝕤/ 𝔹𝕦𝕥𝕥𝕠𝕟𝕤 ℙ𝕖𝕣 ℙ𝕒𝕘𝕖/ 𝕋𝕠𝕥𝕒𝕝 ℝ𝕖𝕤𝕦𝕝𝕥 𝕎𝕚𝕥𝕙𝕠𝕦𝕥 𝔸𝕔𝕦𝕥𝕒𝕝𝕝𝕪 𝔼𝕕𝕚𝕥𝕚𝕟𝕘 𝕋𝕙𝕖 ℝ𝕖𝕡𝕠... 𝔸𝕝𝕤𝕠 𝕀𝕥 ℙ𝕣𝕠𝕧𝕚𝕕𝕖 𝕆𝕡𝕥𝕚𝕠𝕟 𝕋𝕠 𝔼𝕟𝕒𝕓𝕝𝕖/𝔻𝕚𝕤𝕒𝕓𝕝𝕖 𝔽𝕠𝕣 𝕊𝕙𝕠𝕨𝕚𝕟𝕘 𝕀𝕟𝕧𝕚𝕥𝕖 𝕃𝕚𝕟𝕜 𝕀𝕟 𝔼𝕒𝕔𝕙 ℝ𝕖𝕤𝕦𝕝𝕥𝕤🤡</b>

            -> <code>Configure</code> - <b>𝔹𝕦𝕥𝕥𝕠𝕟 𝕎𝕚𝕝𝕝 ℍ𝕖𝕝𝕡𝕤 𝕐𝕠𝕦 𝕋𝕠 ℂ𝕙𝕒𝕟𝕘𝕖 ℕ𝕠. 𝕠𝕗 ℙ𝕒𝕘𝕖𝕤/ 𝔹𝕦𝕥𝕥𝕠𝕟𝕤 ℙ𝕖𝕣 ℙ𝕒𝕘𝕖/ 𝕋𝕠𝕥𝕒𝕝 ℝ𝕖𝕤𝕦𝕝𝕥 𝕎𝕚𝕥𝕙𝕠𝕦𝕥 𝔸𝕔𝕦𝕥𝕒𝕝𝕝𝕪 𝔼𝕕𝕚𝕥𝕚𝕟𝕘 𝕋𝕙𝕖 ℝ𝕖𝕡𝕠... 𝔸𝕝𝕤𝕠 𝕀𝕥 ℙ𝕣𝕠𝕧𝕚𝕕𝕖 𝕆𝕡𝕥𝕚𝕠𝕟 𝕋𝕠 𝔼𝕟𝕒𝕓𝕝𝕖/𝔻𝕚𝕤𝕒𝕓𝕝𝕖 𝔽𝕠𝕣 𝕊𝕙𝕠𝕨𝕚𝕟𝕘 𝕀𝕟𝕧𝕚𝕥𝕖 𝕃𝕚𝕟𝕜 𝕀𝕟 𝔼𝕒𝕔𝕙 ℝ𝕖𝕤𝕦𝕝𝕥𝕤😎</b>
            
            -> <code>Status</code> - <b>𝔹𝕦𝕥𝕥𝕠𝕟 𝕎𝕚𝕝𝕝 𝕊𝕙𝕠𝕨𝕤 𝕋𝕙𝕖 𝕊𝕥𝕒𝕥𝕤 𝕆𝕗 𝕐𝕠𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝😎</b>
            
<b><a href="https://t.me/Mo_Tech_YT">© Mo Tech YT</a></b>
"""
    
    ABOUT_TEXT = """<b>➥ 📃Name</b> : <b>Pro Auto Filter Bot</b>

<b>>➥👨‍💼Developer</b> : <b><a href="https://t.me/Moviechanda_Ower">👤Joker</a></b>

<b>➥ 👨‍💻Editor</b> : <b><a href="https://t.me/Moviechanda_Ower">👤Joker</a></b>

<b>➥ 🗣️Language</b> : <b>Python3<b>

<b>➥ 📚Library</b> : <b><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></b>

<b>➥ Support channel 💻</b> : <b><a href="https://t.me/cinemachandabot">💥Click Me</a></b>
"""
