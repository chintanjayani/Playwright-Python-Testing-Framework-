const puppeteer = require('puppeteer');
const { AxePuppeteer } = require('@axe-core/puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Replace with the URL you want to test
  const url = 'https://automationintesting.online';
  await page.goto(url);

  // Inject Axe and run the accessibility tests
  const results = await new AxePuppeteer(page).analyze();

  console.log('Accessibility Violations:');
  console.log(JSON.stringify(results.violations, null, 2));

  await browser.close();
})();
