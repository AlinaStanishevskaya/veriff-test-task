/// <reference types="cypress" />

context('Verify page', () => {
  beforeEach(() => {
    cy.visit("https://demo.saas-3.veriff.me/");
  })

  it('open in macbook-15', () => {
    cy.viewport("macbook-15");
    cy.screenshot();
    cy.wait(200);
  })

  it('open in ipad-2', () => {
    cy.viewport("ipad-2");
    cy.screenshot();
    cy.wait(200);
  })

  it('open in iphone-x', () => {
    cy.viewport("iphone-x");
    cy.screenshot();
    cy.wait(200);
  })

  it('verify me incontext with default data', () => {
    cy.get('.UnstyledButton-module_base__1a3SB').click();
    
    cy.get('iframe')
    .its("0.contentDocument.body")
    .should("not.be.empty")
    .then((body) => {
      cy.wrap(body)
        .find('.p1o17nau').should('be.visible');
      });
  })

  it('verify me incontext with empty full name', () => {
    cy.get('input[name="name"]').clear();
    cy.get('.UnstyledButton-module_base__1a3SB').click();

    cy.get('iframe')
    .its("0.contentDocument.body")
    .should("not.be.empty")
    .then((body) => {
      cy.wrap(body)
        .find('.p1o17nau').should('be.visible');
      });
  })

  it('verify me incontext with input data', () => {
    cy.get('button[name="language"]').click();
    cy.get('#downshift-0-item-4').click();

    cy.get('input[name="documentCountry"]').type('United');
    cy.get('ul[role="listbox"]').children().should('have.length', 5);
    cy.get('ul[role="listbox"]').children().first().click()
    
    cy.get('button[name="documentType"]').click();
    cy.get('#downshift-2-menu').children().should('have.length', 4);
    cy.get('#downshift-2-item-0').click();

    cy.get('.UnstyledButton-module_base__1a3SB').click();

    cy.get('iframe')
    .its("0.contentDocument.body")
    .should("not.be.empty")
    .then((body) => {
      cy.wrap(body)
        .find('h1').should('have.text', "Lad os få dig verificeret");
      });
  })

  it('verify me with redirect', () => {
    cy.get('button[name="language"]').click();
    cy.get('#downshift-0-item-4').click();
    cy.get('input[value="redirect"]').click();
    cy.get('.UnstyledButton-module_base__1a3SB').click();

    cy.get('h1').should('have.text', 'Lad os få dig verificeret');
  })
})