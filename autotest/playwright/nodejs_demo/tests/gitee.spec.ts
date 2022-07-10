import {test, expect} from "@playwright/test";

test('打开Gitee首页', async ({ page}) => {
    await page.goto('https://www.gitee.com');
    await expect(page).toHaveTitle('Gitee - 企业级 DevOps 研发效能平台');
});

test('登陆', async ({ page }) => {
  await page.goto('https://gitee.com/');
  await page.getByRole('link', { name: '登录' }).click();
  await page.getByPlaceholder('手机／邮箱／个人空间地址').click();
  await page.getByPlaceholder('手机／邮箱／个人空间地址').fill('123@qq.com');
  await page.getByPlaceholder('请输入密码').click();
  await page.getByPlaceholder('请输入密码').press('CapsLock');
  await page.getByPlaceholder('请输入密码').fill('password');
  await page.getByRole('button', { name: '登 录' }).click();
});