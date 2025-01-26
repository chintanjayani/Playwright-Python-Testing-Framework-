const puppeteer = require('puppeteer');
const { AxePuppeteer } = require('@axe-core/puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: true, 
    args: ['--no-sandbox', '--disable-setuid-sandbox'], 
  });
  const page = await browser.newPage();

  const url = 'https://automationintesting.online';
  await page.goto(url);

  const results = await new AxePuppeteer(page).analyze();

  console.log('Accessibility Violations:');
  console.log(JSON.stringify(results.violations, null, 2));

  await browser.close();
})();
