const form_reset = (form) => {
  const inputs = form.querySelectorAll('input');
  const textareas = form.querySelectorAll('textarea');
  const selects = form.querySelectorAll('select');
  inputs.forEach(input => input.value = '');
  textareas.forEach(textarea => textarea.value = '');
  selects.forEach(select => select.value = '');
}

const clear_after_update = (url) => {
  var target = document.getElementById("form_section");
  console.log(url);
  fetch(url)
    .then(response => response.text())
    .then(html => {
      target.innerHTML = html;
    });
}

const request = (() => {
  const params = {};
  const url = window.location.href.split('?');
  url.forEach(a => {
    var queries = a.split('&');
    queries.forEach(b => {
      var query = b.split('=')
      var name = query[0];
      var value = query[1];
      if (value) {
        params[name] = value;
      }
    })
  })
  console.log(params);
  return params;
})();

const filtrar = () => {
  const filterForm = document.querySelector('.filter__form');
  if (!filterForm) return;
  const fields = filterForm.querySelectorAll('input[type="checkbox"]')
  console.log(request["categorias"], request["cidades"]);
  if (filterForm) {
    const currentFilters = {}
    currentFilters['cidades'] = [];
    currentFilters['categorias'] = [];

    filterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      let filterUrl = [];
      const form = e.target;
      const fields = form.querySelectorAll('input[type="checkbox"]')
      fields.forEach((f) => {
        const { name, checked, value } = f;
        const filterIndex = currentFilters[name].indexOf(value);

        if (checked && value.length > 0 && filterIndex == -1) {
          currentFilters[f.name].push(f.value);
        }
        if (filterIndex > -1 && !checked) {
          currentFilters[f.name].splice(filterIndex, 1);
        }
      })

      for (const filter in currentFilters) {
        if (currentFilters[filter].length > 0) {
          filterUrl.push(`${filter}=${currentFilters[filter]}`)
        }
      }

      window.location = `/buscar?${filterUrl.join('&')}`

    })
  }

  const qCategorias = request["categorias"]
  const qCidades = request["cidades"]

  console.log(fields);
  fields.forEach(inpt => {
    var existCategoria = qCategorias.indexOf(inpt.value) > -1
    var existCidade = qCidades.indexOf(escape(inpt.value.replace(', ', '  '))) > -1
    if (existCategoria || existCidade) {
      inpt.checked = true;
    }
  })


}

filtrar();

const formsLoad = () => {

  const contatoForm = document.querySelector(".contato__form");
  const newsletterForm = document.querySelector(".newsletter__form");

  contatoForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const form = e.target;
    const fields = form.querySelectorAll('input[type=text],input[type=email],textarea,select')
    const errorSummarty = document.querySelector('.error__summary');
    errorSummarty.innerHTML = "";
    errors = []
    formData = {}
    fields.forEach((field) => {
      const { required, name, value, pattern } = field
      field.classList.remove('invalid-error');
      field.classList.remove('required-error');

      if (required && (value.length == 0)) {
        errors.push(`Campo '${name}' obrigatório`);
        field.classList.add('required-error');
      }

      if (!(new RegExp(pattern).test(value))) {
        errors.push("E-mail invalido.")
        field.classList.add('invalid-error');
      }
      formData[name] = value;
    })

    if (errors.length > 0) {
      errors.forEach((error) => {
        errorSummarty.innerHTML += `<li>${error}</li>`;
      })
    } else {
      fetch('/contato/register', {
        method: 'POST',
        body: JSON.stringify(formData),
        headers: {
          "Content-Type": "application/json"
        }
      }).then((res) => res.json()).then((res) => {
        form.reset();
        alert("Contato enviado com sucesso!")
      })
    }
    console.log(errors);
  })

  newsletterForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const form = e.target;
    const fields = form.querySelectorAll('input[type=email]')
    const errors = []
    const formData = {}
    fields.forEach((field) => {
      const { required, name, value, pattern } = field
      field.classList.remove('invalid-error');
      field.classList.remove('required-error');

      if (required && (value.length == 0)) {
        errors.push(`Campo '${name}' obrigatório`);
        field.classList.add('required-error');
      }

      if (!(new RegExp(pattern).test(value)) && value.length > 0) {
        errors.push("E-mail invalido.")
        field.classList.add('invalid-error');
      }
      formData[name] = value;
    })

    if (errors.length > 0) {
      alert(errors.join("/n"))
    } else {
      fetch('/newsletter/subscribe', {
        method: 'POST',
        body: JSON.stringify(formData),
        headers: {
          "Content-Type": "application/json"
        }
      }).then((res) => res.json()).then((res) => {
        form.reset();
        alert("Inscrito com sucesso!")
      })

    }
  });
}

formsLoad();