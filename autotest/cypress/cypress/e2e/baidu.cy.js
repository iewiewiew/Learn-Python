describe('Demo of searching in baidu', function () {
  var text = 'Cypress';
  before(() => {
    cy.log('I will run before all');
  })
  beforeEach(() => {
    cy.visit('http://www.baidu.com')
  })
  it('I search the text by baidu', function () {
    cy.get('#kw').type(text);
    cy.get('#kw').should('have.value', text)
    cy.url().should("contains", "baidu")
  })
  it('Should search cypress教程 success ', function () {
    cy.get('input.s_ipt').type('cypress教程');
    cy.get('#kw').should('have.value', 'cypress教程')
  })
  afterEach(() => {
    cy.log('I will run after each');
  })
  after(() => {
    cy.log('I will run after all');
  })
})