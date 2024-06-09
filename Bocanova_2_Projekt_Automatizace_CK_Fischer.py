def test_fischer_kontakty(page):
  #najít na webové stránce www.fischer.cz odkaz na "Kontakty"
  page.goto('https://www.fischer.cz/')
  from selenium.webdriver.common.by import By
  locator = (By.CSS_SELECTOR, 'a.f_anchor[href="/kontakty"]')
  #test proběhl úspěšně - na webové stránce www.fischer.cz je odkaz na "Kontakty"
  #webová stránka se sama zavřela



def test_fischer_odlety_z_pardubic(page):
  #naít na webové stránce www.fischer.cz přímý odkaz na "Letenky" ověřit jeho funkčnost.
  page.goto('https://www.fischer.cz/')
  # čekám na okno "Nastavení soukromí"
  accept_button = page.get_by_role("button", name="Přijmout vše")
  accept_button.click()
  #"letenky"
  page.click('span.segmentation-list-text[data-v-8b33c410]')
  #test proběhl úspěšně - na webové stránce www.fischer.cz je odkaz na "letenky" a klik na něj funguje.
  #stránka se sama zavřela.



def test_fischer_registrace_do_newsletteru(page):
  #najít na webové stránce www.fischer.cz okno pro vepsání emailu a registrace do newsletteru.
  page.goto('https://www.fischer.cz/')
  #čekám na okno "Nastavení soukromí"
  accept_button = page.get_by_role("button", name="Přijmout vše")
  accept_button.click()
  # vyhledat okno pro vepsání emailu
  locator = 'label[for="input-email-1"]'
  # Najít element na stránce
  email_label = page.locator(locator)
  # Kliknout na nalezený element
  email_label.click()
  #Vyplnění vstupního pole hodnotou "Ahoj@centrum.cz"
  email_label.fill("Ahoj@centrum.cz")
  #Lokátor pro tlačítko "Registrovat"
  submit_button = page.locator('div.whitespace-nowrap.overflow-ellipsis.overflow-hidden:has-text("Registrovat")')
  # Kliknutí na tlačítko "Registrovat"
  submit_button.click()
  #test proběhl úspěšně - objevilo se okno s poděkování a odesláním formuláře a stránka se zavřela.







